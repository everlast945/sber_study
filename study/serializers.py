from django.db import transaction
from rest_framework import serializers

from study.models import Intern, Subject, InternSubject, Direction


# region Постапающие

class InternListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = (
            'id',
            'fio',
            'birthday_year',
            'passport_number',
        )


class InternSubjectSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source='subject.name')

    class Meta:
        model = InternSubject
        fields = (
            'score',
            'name',
        )


class InternRetrieveSerializer(serializers.ModelSerializer):
    subjects = InternSubjectSerializer(many=True, source='intern_subjects')

    class Meta:
        model = Intern
        fields = (
            'id',
            'fio',
            'birthday_year',
            'passport_number',
            'subjects',
        )


class InternSubjectCreateUpdateSerializer(serializers.Serializer):
    score = serializers.CharField()
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all())


class InternCreateUpdateSerializer(serializers.ModelSerializer):
    subjects = InternSubjectCreateUpdateSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Intern
        fields = (
            'id',
            'fio',
            'birthday_year',
            'passport_number',
            'subjects',
        )

    @transaction.atomic
    def create(self, validated_data):
        subjects = validated_data.pop('subjects', None)
        intern = super().create(validated_data)
        intern.save_subjects(subjects)
        return intern

    @transaction.atomic
    def update(self, instance, validated_data):
        subjects = validated_data.pop('subjects', None)
        intern = super().update(instance, validated_data)
        intern.save_subjects(subjects)
        return intern


# endregion

# region Предметы


class SubjectListRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'id',
            'name',
            'min_score',
        )


class SubjectCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'id',
            'name',
            'min_score',
        )

# endregion

# region Направления


class DirectionListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = (
            'id',
            'name',
        )


class DirectionInternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = (
            'id',
            'fio',
        )


class DirectionSubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = (
            'id',
            'name',
            'min_score',
        )


class DirectionRetrieveSerializer(serializers.ModelSerializer):
    interns = DirectionInternSerializer(many=True)
    subjects = DirectionSubjectSerializer(many=True)

    class Meta:
        model = Direction
        fields = (
            'id',
            'name',
            'interns',
            'subjects',
        )


class DirectionCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direction
        fields = (
            'id',
            'name',
        )

# endregion