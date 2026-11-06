from pathlib import Path

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import Session, DeclarativeBase, relationship

# Файл базы данных появится автоматически рядом с main.py
DB_PATH = Path(__file__).with_name("test.db")
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)


class Base(DeclarativeBase):
    pass


class Groups(Base):
    __tablename__ = "groups"

    group_id = Column(Integer, primary_key=True, index=True)
    group_name = Column(String, nullable=False)
    course = Column(Integer, nullable=False)

    students = relationship("Students", back_populates="group")


class Students(Base):
    __tablename__ = "students"

    student_id = Column(Integer, primary_key=True, index=True)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    group_id = Column(Integer, ForeignKey("groups.group_id"))

    group = relationship("Groups", back_populates="students")


def create_and_fill_database():
    # Создаёт таблицы, если их ещё нет
    Base.metadata.create_all(engine)

    with Session(engine) as db:
        # Заполняем базу только при первом запуске
        if db.query(Groups).count() == 0:
            db.add_all([
                Groups(group_id=1, group_name="ИС-21", course=2),
                Groups(group_id=2, group_name="ИС-22", course=1),
                Groups(group_id=3, group_name="ПМ-21", course=2),
                Groups(group_id=4, group_name="ЭК-23", course=1),
            ])
            db.commit()

        if db.query(Students).count() == 0:
            db.add_all([
                Students(last_name="Иванов", first_name="Алексей", group_id=1),
                Students(last_name="Петрова", first_name="Мария", group_id=1),
                Students(last_name="Сидоров", first_name="Дмитрий", group_id=1),
                Students(last_name="Кузнецова", first_name="Анна", group_id=2),
                Students(last_name="Смирнов", first_name="Игорь", group_id=2),
                Students(last_name="Волкова", first_name="Елена", group_id=2),
                Students(last_name="Морозов", first_name="Павел", group_id=3),
                Students(last_name="Зайцева", first_name="Ольга", group_id=3),
                Students(last_name="Лебедев", first_name="Никита", group_id=3),
                Students(last_name="Козлова", first_name="Дарья", group_id=4),
                Students(last_name="Новиков", first_name="Артём", group_id=4),
                Students(last_name="Соколова", first_name="Виктория", group_id=1),
            ])
            db.commit()


def show_groups():
    print("\n========== СПИСОК ГРУПП ==========")
    with Session(engine) as db:
        groups = db.query(Groups).order_by(Groups.group_id).all()
        for group in groups:
            print(
                f"ID:{group.group_id} "
                f"Название группы: {group.group_name} "
                f"Курс: {group.course}"
            )


def show_students():
    print("\n========== СПИСОК СТУДЕНТОВ ==========")
    with Session(engine) as db:
        students = db.query(Students).order_by(Students.student_id).all()
        for student in students:
            group_name = student.group.group_name if student.group else "не указана"
            print(
                f"ID:{student.student_id} "
                f"ФИ: {student.last_name} {student.first_name} "
                f"Группа: {group_name}"
            )


if __name__ == "__main__":
    create_and_fill_database()
    show_groups()
    show_students()
    print(f"\nБаза данных сохранена: {DB_PATH}")
    print("\nГотово! Программа выполнилась без ручного ввода SQL.")
