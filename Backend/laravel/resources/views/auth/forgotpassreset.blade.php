<!-- resources/views/auth/reset.blade.php -->

<form method="POST" action="{{route('forgotpass.form')}}">
    {!! csrf_field() !!}
    <input type="hidden" name="token" value="{{ $token }}">
    <div>
        Email
        <input type="email" name="email" value="{{ old('email') }}">
    </div>

    <div>
        Password
        <input type="password" name="password">
    </div>

    <div>
        Confirm Password
        <input type="password" name="password_confirmation">
    </div>

    <div>
        <button type="submit">
            Reset Password
        </button>
    </div>
</form>

@if($errors->any())
    <div class="alert alert-danger">
        {{$errors->first()}}
    </div>
@endif