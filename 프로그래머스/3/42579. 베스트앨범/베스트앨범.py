# 장르별 가장 많이 재생된 노래 두개씩

# 속한 노래가 많이 재생된 장르 먼저 
# 장르 내 많이 재생된 노래 먼저
# 재생 횟수가 같으면 고유 번호 낮은 노래 먼저

# 장르별 총 재생 횟수 계산
# 각 장르 내 노래별 재생 횟수 계산
# 장르별 상위 두 곡 선택
# 장르별 정렬

from collections import defaultdict
    
def solution(genres, plays):
    
    genre_total = defaultdict(int)
    genre_songs = defaultdict(list)
    
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        
        genre_total[genre] += play
        genre_songs[genre].append((play, i))
    
    # 장르를 총 재생 횟수 기준으로 내림차순 정렬
    sorted_genres = sorted(genre_total.items(), key=lambda x: x[1], reverse=True)
    
    # 장르별 상위 두 곡 선택
    result = []
    
    for genre, _ in sorted_genres:
        
        # 각 장르별 노래를 재생 횟수 기준으로 내림차순 정렬 (같은 재생 횟수는 고유 번호 기준으로 오름차순)
        sorted_songs = sorted(genre_songs[genre], key=lambda x: (-x[0], x[1]))
        # 상위 두 곡 추가
        result.extend(song[1] for song in sorted_songs[:2])
    
    return result


# sorted() 함수의 key
# 리스트 정렬 시의 기준이 되는 값을 계산하는 함수 전달
# 이 함수는 리스트 각 항목에 적용돼 정렬 기준 값 반환

# lambda x: x[1]
# lambda 함수 -> python에서 익명 함수(이름 없는 함수)를 정의하는 방법. 이름 없고, 간단한 '식'으로 함수 정의
# x -> lambda 함수가 받는 입력값. sorted()에 의해 리스트 각 요소들이 x로 전달됨. 현재 상황에서는 튜플 (장르, 총 재생 횟수)
# x[1] -> x의 인덱스 1값. 즉 튜플의 두번째 요소인 재생 횟수
# 즉 lambda x: x[1]는, 인자 x를 받는 lambda 함수의 리턴값이 x[1]이라는 것
# 따라서 각 항목의 두번째 요소를 정렬 기준으로 사용하겠다는 의미



