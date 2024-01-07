def extract(test_index):
    task1_reading = str(open(f'../downloaded_resources/Speaking/Task1/Reading/TPO{test_index}.txt').read())

    task2_reading = str(open(f'../downloaded_resources/Speaking/Task2/Reading/TPO{test_index}.txt').read())
    task2_listening = str(f'/downloaded_resources/Speaking/Task2/Listening/TPO{test_index}.mp3')
    task2_transcript = str(open(f'../downloaded_resources/Speaking/Task2/Transcripts/TPO{test_index}.txt').read())

    task3_reading = str(open(f'../downloaded_resources/Speaking/Task3/Reading/TPO{test_index}.txt').read())
    task3_listening = str(f'/downloaded_resources/Speaking/Task3/Listening/TPO{test_index}.mp3')
    task3_transcript = str(open(f'../downloaded_resources/Speaking/Task3/Transcripts/TPO{test_index}.txt').read())

    task4_listening = str(f'/downloaded_resources/Speaking/Task4/Listening/TPO{test_index}.mp3')
    task4_transcript = str(open(f'../downloaded_resources/Speaking/Task4/Transcripts/TPO{test_index}.txt').read())

    return [[task1_reading], [task2_reading, task2_listening, task2_transcript],
            [task3_reading, task3_listening, task3_transcript], [task4_listening, task4_transcript]]

