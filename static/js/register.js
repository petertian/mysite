$(function(){
	var MsgRequest = [];
		MsgRequest[0] = '';
		MsgRequest[1] = '* You must enter a password!';
		MsgRequest[2] = '* password is too short!';
		MsgRequest[3] = '* no symbol allow in password';
	var	result = true,
		tipsspeed = 200;
	var _password = _confirmpassword = '';

	$('#password').focus(function(){$(this).addClass('focusinput').removeClass('normalinput');})
	              .blur(function(){$(this).addClass('normalinput').removeClass('focusinput');pwdCheck(this);//密码验证
	});
  	$('#confirmpassword').focus(function(){$(this).addClass('focusinput').removeClass('normalinput');})
	              .blur(function(){$(this).addClass('normalinput').removeClass('focusinput');pwdconfirmCheck(this);//密码验证
	});
	
	function pwdCheck(obj){
		/* 1, 密码不能为空
 		   2，长度不短于6个字符
 		   3，不能含有空格
		*/
		var str = $(obj).val();
		if(str.length < 6){
			if(str.length < 1){
				$(obj).siblings('p').slideDown(tipsspeed).html(MsgRequest[1]);
			}else{
				$(obj).siblings('p').slideDown(tipsspeed).html(MsgRequest[2]);
			}
			//$(obj).removeClass('focusinput').addClass('errorinput');
			$(obj).siblings('i').eq(0).hide();
			$(obj).siblings('i').eq(1).show();
			result = false;
		}else{
			if(!result){
				inputReset(obj);
			}
		}
	};

	function pwdconfirmCheck(obj){
		if($(obj).val() != $('#password').val()){
			$(obj).siblings('p').slideDown(tipsspeed).html(MsgRequest[4]);
			$(obj).siblings('i').eq(0).hide();
			$(obj).siblings('i').eq(1).show();
			result = false;
		}else{
			if(!result){
				inputReset(obj);
				result = true;
			}
		}
	};

	function inputReset(obj){
		$(obj).siblings('p').slideUp(tipsspeed);
		$(obj).siblings('i').eq(0).show();
		$(obj).siblings('i').eq(1).hide();
	};

	$('#login').submit(function(){
		alert('a');
		console.log(result);
		if(result){}
		else{ return false;}
	});

});