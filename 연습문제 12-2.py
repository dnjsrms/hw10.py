import pickle
import os

def input_scores():
    s = []
    i = 1
    while True:
        n = int(input(f'#{i}? '))
        if n < 0:
            break
        s.append(n)
        i += 1
    return s

def get_average(s):
    return sum(s) / len(s)

def show_scores(s):
    for n in s:
        print(n, end=' ')
    print()

def save_scores(scores, filename='score.bin'):
    with open(filename, 'wb') as f:
        pickle.dump(scores, f)

def load_scores(filename='score.bin'):
    if os.path.exists(filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)
    return None

# 메인 프로그램
scores = load_scores()
if scores is None:
    print('[점수 입력]')
    scores = input_scores()
    save_scores(scores)
else:
    print('[파일 읽기]')

print('\n[점수 출력]\n개인점수: ', end=' ')
show_scores(scores)
avg = get_average(scores)
print(f'평균: {avg:.1f}')
print()

print('[검색]')
s = int(input('찾고자 하는 점수는? '))
if s in scores:
    idx = scores.index(s)
    print(f'{s}점은 {idx + 1}번 학생의 점수입니다.')
else:
    print(f'{s}점을 받은 학생은 없습니다.')
