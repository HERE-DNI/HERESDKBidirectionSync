---
title: "AuthenticationModeAccessTokenProvider typedef"
slug: "sdk-for-flutter-navigate-core-engine-authenticationmodeaccesstokenprovider"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- AuthenticationModeAccessTokenProvider.html -->


<div>
<h1>AuthenticationModeAccessTokenProvider typedef</h1></div>

AuthenticationModeAccessTokenProvider =
     String? Function()


<p>This lambda is used to retrieve access token in synchronous manner.</p>
<p>It returns the access token or null if it is not set.
The lambda is called each time the access token is needed and it is executed
on the main thread of the application.</p>
<p>Returns Access token in case it is set or null otherwise.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">typedef AuthenticationModeAccessTokenProvider = String? Function();</code></pre>

 



</div>
`
}</HTMLBlock>
