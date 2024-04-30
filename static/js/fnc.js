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
    success: function (data) {},
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
