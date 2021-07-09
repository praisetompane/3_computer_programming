from undo_operations import OperationsUndoer

def main():
    print("Praise typing his body of knowldge")
    text_processor = OperationsUndoer("")
    print("My blank slate")
    text_processor.display()
    text_processor.add_operations_result("I")
    text_processor.add_operations_result(" ")
    text_processor.add_operations_result("k")
    text_processor.add_operations_result("m")
    text_processor.undo()
    text_processor.add_operations_result("n")
    text_processor.add_operations_result("o")
    text_processor.add_operations_result("w")
    print("Try undo and redo")
    text_processor.undo()
    text_processor.redo()
    text_processor.add_operations_result(" that")
    text_processor.undo()


if __name__ == "__main__":
    main()