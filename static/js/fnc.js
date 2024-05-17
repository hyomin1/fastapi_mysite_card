// 카카오 나에게 메세지 보내기

/** DESIGN **/
const kakao_label = document.querySelectorAll(".kakao_input_label");
kakao_label.forEach((label) => {
  label.addEventListener("click", onClickLabel);
});

function onClickLabel() {
  $(this)
    .css("top", "-22%")
    .css("font-size", "1.2rem")
    .css("padding", "0.7rem");
  $(this).prev().css("opacity", "1").focus();
}

const kakao_input = document.querySelectorAll(".kakao_input");
kakao_input.forEach((input) => {
  input.addEventListener("blur", onBlurInput);
});

function onBlurInput() {
  if (this.value == "" || this.value.length == 0) {
    this.style.opacity = 0;
    $(this)
      .next()
      .css("top", ".8rem")
      .css("font-size", "1.6rem")
      .css("padding", "0");
  }
}

/** EVENT **/
document.querySelector(".kakao_btn").addEventListener("click", function () {
  $(this).css("display", "none");
  $("#kakao_wrap").css("display", "block");
  $(".kakao_close_btn").css("display", "flex");
});

function close_kakao() {
  document.querySelector("#kakao_wrap").style.display = "none";
  document.querySelector(".kakao_close_btn").style.display = "none";
  document.querySelector(".kakao_btn").style.display = "flex";
}

/** FUNCTION **/
function sendKakao() {
  msg = {
    name: document.querySelector("#kakao_name").value,
    email: document.querySelector("#kakao_email").value,
    message: document.querySelector("#kakao_message").value,
  };

  // 동기 : 페이지가 처음부터 렌더링 -> Default
  // 비동기 : 현재 그대로 유지한 상태로 원하는 값만 변경 -> AJAX
  $.ajax({
    url: "/kakao/", // http://127.0.0.1:8000/kakao
    data: JSON.stringify(msg),
    type: "POST",
    contentType: "application/json; charset=utf-8",
    dataType: "JSON",
    success: function (data) {
      document.querySelector("#kakao_form").reset();
      document.querySelector("#kakao_wrap").style.display = "none";
      document.querySelector(".kakao_close_btn").style.display = "none";
      document.querySelector(".kakao_btn").style.display = "flex";
    },
    error: function (data) {
      console.log(data);
    },
  });
}

// 일반
$(document).ready(function () {
  $("#send_kakao_btn").click(function () {
    sendKakao();
  });

  // Scroll TOP버튼 생성 및 TOP으로 이동
  $(window).scroll(function () {
    // 스크롤이 움직이면
    if (
      document.body.scrollTop > 80 ||
      document.documentElement.scrollTop > 80
    ) {
      $(".top_btn").fadeIn().css("display", "flex");
    } else {
      $(".top_btn").fadeOut();
    }
  });
  $(".top_btn").click(function () {
    $("html, body").animate({ scrollTop: 0 }, 800);
  });
});

// 챗봇(ChatGPT) 메시지 주고받기

/** EVENT **/

document.querySelector(".chatbot_btn").addEventListener("click", function () {
  $(this).css("display", "none");

  $("#kakao_wrap").css("display", "none");

  $(".kakao_btn").css("display", "flex");

  $(".kakao_close_btn").css("display", "none");

  $("#chatbot_wrap").css("display", "block");

  $(".chatbot_close_btn").css("display", "flex");

  let today = new Date();

  var options = { hour: "numeric", minute: "numeric" };

  now_time = today.toLocaleTimeString("ko-KR", options);

  document.querySelector(".chat_msg_date").innerHTML = now_time;
});

function close_chatbot() {
  document.querySelector("#chatbot_wrap").style.display = "none";

  document.querySelector(".chatbot_close_btn").style.display = "none";

  document.querySelector(".chatbot_btn").style.display = "flex";
}

/** FUNCTION **/

function view_human(txt) {
  // 사용자 메세지 챗 디자인

  let today = new Date();

  var options = { hour: "numeric", minute: "numeric" };

  msg = ` 

          <div class="human_msg_box"> 

              <div class="chat_msg_box_right">

                  <span class="chat_msg_date">${today.toLocaleTimeString(
                    "ko-KR",
                    options
                  )}</span>

                  <span class="chat_msg_info">${txt}</span> 

              <div> 

          </div> 

      `;

  return msg;
}

document.querySelector("#send_chat_btn").onclick = function () {
  var txt = document.querySelector("#send_chat_input").value;

  if (txt.length != 0 || txt != "") {
    send_chat_server(txt);
  } else {
    console.log("메세지를 입력해주세요.");
  }
};

function enter_keypress(e) {
  var txt = document.querySelector("#send_chat_input").value;

  if (txt.length != 0 || txt != "") {
    var code = e.code;

    if (code == "Enter") {
      send_chat_server(txt);
    }
  } else {
    console.log("메세지를 입력해주세요.");
  }
}

// 챗봇 메세지 디자인

function view_chatbot(answer) {
  let today = new Date();

  var options = { hour: "numeric", minute: "numeric" };

  msg = `

      <div class="chat_msg_box">

          <div class="chat_msg_box_left">

              <i class="fas fa-robot"></i>

          </div>

          <div class="chat_msg_box_right">

              <span class="chat_msg_date">${today.toLocaleTimeString(
                "ko-KR",
                options
              )}</span>

              <span class="chat_msg_info">${answer} </span>

          </div>

      </div>

  `;

  return msg;
}

function moveScroll() {
  const chat_box = document.querySelector(".msg_box");

  console.log("top: " + chat_box.scrollTop);

  console.log("height: " + chat_box.scrollHeight);

  if (chat_box.scrollHeight > 0) chat_box.scrollTop = chat_box.scrollHeight;
}

function send_chat_server(txt) {
  document.querySelector("#send_chat_input").value = "";

  // 사용자 챗(질문) 출력

  const chat_box = document.querySelector(".msg_box");

  const nowScrollY = chat_box.scrollTop;

  chat_box.insertAdjacentHTML("beforeend", view_human(txt));

  moveScroll();

  // 챗봇 챗(답변) 출력

  console.log(txt);

  if (txt.length > 0 || txt != "") {
    $.ajax({
      url: "/chat/",

      data: JSON.stringify({ question: txt }),

      type: "POST",

      contentType: "application/json; charset=UTF-8",

      dataType: "json",

      success: function (data) {
        console.log(data["answer"]);

        chat_box.insertAdjacentHTML("beforeend", view_chatbot(data["answer"]));

        moveScroll();
      },

      error: function (data) {
        console.log(data);
      },
    });
  } else {
    console.log("문자열을 입력해주세요.");
  }
}
