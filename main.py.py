import time

def typing_speed_test():
    print("Type the following sentence as fast as you can:")
    test_sentence = "Physics is a branch of science that studies the natural world and the behavior of matter and energy in it. It involves exploring the fundamental principles that govern the behavior of matter and energy, as well as the interactions between them."
    print(test_sentence)
    input("Press Enter when you're ready to start...")

    start_time = time.time()

    user_input = input()

    end_time = time.time()

    time_taken = end_time - start_time
    words_typed = len(user_input.split())
    typing_speed = words_typed / time_taken

    print("Time taken: {:.2f} seconds".format(time_taken))
    print("Words typed: {}".format(words_typed))
    print("Typing speed: {:.2f} words per second".format(typing_speed))

typing_speed_test()
