<!-- resources/views/auth/password.blade.php -->

<form method="POST" action="{{route('email.password.post')}}">
    {!! csrf_field() !!}

    <div>
        Email
        <input type="email" name="email" value="{{ old('email') }}">
    </div>

    <div>
        <button type="submit">
            Enviar Redefinicao de Senha
        </button>
    </div>
</form>

@if($errors->any())
    <div class="alert alert-danger">
        {{$errors->first()}}
    </div>
@endif

@if(!empty($success))
    <div class="alert alert-success">
        {{ $success }}
    </div>
@endif