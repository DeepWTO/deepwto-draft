def count_correct_pred(prediction, batch_labels):
    TFPN = None
    count_label_one = 0
    count_label_zero = 0
    count_correct_one = 0
    count_correct_zero = 0
    for idx, batch_label in enumerate(batch_labels):
        if batch_label == [1]:
            count_label_one += 1
        if batch_label == [1] and prediction[idx] == 0.5:
            print("------------------------------")
            print("EVEN FOR POSITIVE LABEL")
            print("batch_label", batch_label)
            print("after_sigmoid", prediction[idx])
        if batch_label == [1] and prediction[idx] > 0.5:
            TFPN = "TRUE POSITIVE"
            print("------------------------------")
            print("TRUE POSITIVE")
            count_correct_one += 1
            print("batch_label", batch_label)
            print("after_sigmoid", prediction[idx])
        if batch_label == [1] and prediction[idx] < 0.5:
            TFPN = "FALSE NEGATIVE"
            print("------------------------------")
            print("FALSE NEGATIVE!")
            print("batch_label", batch_label)
            print("after_sigmoid", prediction[idx])

        if batch_label == [0]:
            count_label_zero += 1
        if batch_label == [0] and prediction[idx] == 0.5:
            print("------------------------------")
            print("EVEN FOR NEGATIVE LABEL")
            print("batch_label", batch_label)
            print("after_sigmoid", prediction[idx])
        if batch_label == [0] and prediction[idx] > 0.5:
            TFPN = "FALSE NEGATIVE"
            print("------------------------------")
            print("FALSE NEGATIVE!")
            print("batch_label", batch_label)
            print("after_sigmoid", prediction[idx])
        elif batch_label == [0] and prediction[idx] < 0.5:
            TFPN = "TRUE NEGATIVE"
            print("------------------------------")
            print("TRUE NEGATIVE!")
            print("batch_label", batch_label)
            print("after_sigmoid", prediction[idx])
            count_correct_zero += 1

    return count_label_one, \
           count_label_zero, \
           count_correct_one, \
           count_correct_zero, \
           TFPN
