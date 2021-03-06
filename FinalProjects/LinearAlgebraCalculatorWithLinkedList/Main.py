from FinalProjects.LinearAlgebraCalculatorWithLinkedList.FilesAndData import FilesAndData
from FinalProjects.LinearAlgebraCalculatorWithLinkedList.Vectors import Vectors
from FinalProjects.LinearAlgebraCalculatorWithLinkedList.Matrix import Matrix


class Main:

    @staticmethod
    def main():
        print("Hello this is the linear algebra calculator which works with Linked List to make operations faster!")
        file = FilesAndData.list_and_change_file()
        while True:
            FilesAndData.print_all(0)
            show_or_calculate = input("> ")
            if show_or_calculate == "1" or show_or_calculate == "2":
                wish = input('''\nEnter "1" if you want to save all calculated data.
                                \rOtherwise enter anything else. \n> ''')
                if show_or_calculate == "1":
                    Vectors.vector_operations(wish, file)
                elif show_or_calculate == "2":
                    Matrix.matrix_operations(wish, file)
            elif show_or_calculate == "3":
                file.show_or_manipulate_data()
            elif show_or_calculate == "4":
                file = FilesAndData.list_and_change_file()
            else:
                file.exit_and_save()
                print('Bye!')
                break


if __name__ == "__main__":
    Main.main()
