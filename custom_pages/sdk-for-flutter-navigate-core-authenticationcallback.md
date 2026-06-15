---
title: "AuthenticationCallback typedef"
slug: "sdk-for-flutter-navigate-core-authenticationcallback"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AuthenticationCallback.html -->


<div>
<h1>AuthenticationCallback typedef</h1></div>

AuthenticationCallback =
     void Function(<a href="sdk-for-flutter-navigate-core-authenticationerror">AuthenticationError</a>? authenticationError, <a href="sdk-for-flutter-navigate-core-authenticationdata-class">AuthenticationData</a>? authenticationData)


<p>Callback passed to <a href="sdk-for-flutter-navigate-core-authentication-authenticatewithsdknativeengine">Authentication.authenticateWithSDKNativeEngine</a>.</p>
<p>This callback is called on the main thread asynchronously when an
authenticate call has completed.</p>
<ul>
<li>
<p><code>authenticationError</code> Represents the operation status. It is 'null' for an operation that succeeds.</p>
</li>
<li>
<p><code>authenticationData</code> Represents the authentication data.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef AuthenticationCallback = void Function(AuthenticationError? authenticationError, AuthenticationData? authenticationData);</code></pre>

 



</div>
`
}</HTMLBlock>
