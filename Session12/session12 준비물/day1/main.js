function play(e) {
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`li[data-key="${e.keyCode}"]`);
  // 1. audio 변수를 html에서 select해주세요. audio변수는 누르는 키보드에 헤당하는 keycode를 가지고 있는 음악파일입니다.
  // 2. key 변수를 html에서 select해주세요. key 변수는 누르는 키보드에 헤당하는 keycode를 가진 li 태그입니다.
  if (audio) {
    audio.play();
    key.classList.add('play');
  };
};

// const 상수, function 은 함수 (e)
// audio - html 의 audio , e.KeyCode
// querySelector: dom 은 html 에서 태그들을 지칭, css선택자를 이용해서 선택할 수 있게 하는 것
// key.classList.add('play') -> li 태그의 클래스에다가 play라는 클래스를 추가..


function pause(e){
  // 1. audio 변수를 html에서 select해주세요. audio변수는 누르는 키보드에 헤당하는 keycode를 가지고 있는 음악파일입니다.
  // 2. key 변수를 html에서 select해주세요. key 변수는 누르는 키보드에 헤당하는 keycode를 가진 li 태그입니다.
  const audio = document.querySelector(`audio[data-key="${e.keyCode}"]`);
  const key = document.querySelector(`li[data-key="${e.keyCode}"]`);
  if (audio) {
    audio.currentTime = 0;
    audio.pause();
    key.classList.remove('play');
    //    3. 누른 key에 play 클래스를 제거하세요
  }
};


// 4. 키보드를 눌렀을때 play함수가 실행되게, 키보드를 뗀다면 pause함수가 실행되게 해주세요

document.addEventListener('keydown',play);
document.addEventListener('keyup',pause);


// eventlistener: 특정 이벤트가 발생했을 때 특정 함수를 실행하게하는 매소드. 이벤트-keydown, keyup
// play 랑 pause 정의하기