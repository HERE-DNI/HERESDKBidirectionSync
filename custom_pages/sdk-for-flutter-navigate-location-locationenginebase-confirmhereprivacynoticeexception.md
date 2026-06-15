---
title: "confirmHEREPrivacyNoticeException abstract method"
slug: "sdk-for-flutter-navigate-location-locationenginebase-confirmhereprivacynoticeexception"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- confirmHEREPrivacyNoticeException.html -->


<div>
<h1>confirmHEREPrivacyNoticeException abstract method</h1></div>

<a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>
confirmHEREPrivacyNoticeException()

      

    

<p>By calling this method, the application developer confirms that they have received an exceptional permission
from HERE in written form to <strong>not</strong> include a reference to the HERE Privacy Notice.</p>
<p>As a result,
the <code>LocationEngine</code> will not collect characteristic information about the nearby mobile and Wi-Fi network signals.
However, the engine will still be fully functional and it will deliver location updates when the exception
can be confirmed.
Note that this call should not involve user interaction and it should be executed silently
by the application before starting the <code>LocationEngine</code>.</p>
<p>The permission for exceptional use will be verified asynchronously using your HERE SDK credentials.
A missing permission will lead to stopping of the <code>LocationEngine</code> and <a href="sdk-for-flutter-navigate-location-locationenginestatus">LocationEngineStatus.privacyNoticeUnconfirmed</a>
is delivered to <code>LocationStatusListener</code>.</p>
<p>It is not necessary to call this method on iOS platform.</p>
<p>Returns <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>. Confirmation action status. Valid values are defined in <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>.
A first-time call may result in <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus.pending</a>, make sure to use the
<code>LocationStatusListener</code> to get notified on an unconfirmed permission.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ConfirmationStatus confirmHEREPrivacyNoticeException();</code></pre>

 



</div>
`
}</HTMLBlock>
