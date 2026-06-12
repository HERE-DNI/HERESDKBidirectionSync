---
title: "confirmHEREPrivacyNoticeException method"
slug: "sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeexception"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- confirmHEREPrivacyNoticeException.html -->


<div>
<h1>confirmHEREPrivacyNoticeException method</h1></div>

<a href="/sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>
confirmHEREPrivacyNoticeException()

      <div class="features">override</div>


<p>On Android devices by calling this method, the application developer confirms that they have received an
exceptional permission from HERE in written form to <strong>not</strong> include a reference to the HERE
Privacy Notice. As a result, the <code>LocationEngine</code> will not collect characteristic
information about the nearby mobile and Wi-Fi network signals. However, the engine will still
be fully functional and will deliver location updates when the exception can be confirmed.</p>
<p><strong>Note:</strong> This call should not involve user interaction and should be executed silently
by the application before starting the <code>LocationEngine</code>.</p>
<p>The permission for exceptional use will be verified asynchronously using your HERE SDK
credentials. A missing permission will cause the <code>LocationEngine</code> to stop, and
<code>LocationEngineStatus.PRIVACY_NOTICE_UNCONFIRMED</code> will be delivered to the
<code>LocationStatusListener</code>.</p>
<p>Returns:</p>
<ul>
<li>A confirmation action status. Valid values are defined in <a href="/sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>.</li>
<li>A first-time call may result in <code>ConfirmationStatus.PENDING</code>. Ensure that the
<code>LocationStatusListener</code> is used to get notified if permission remains unconfirmed.</li>
</ul>
<p>On iOS devices this method does nothing and <a href="/sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus.ok</a> is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ConfirmationStatus confirmHEREPrivacyNoticeException() =&gt;
    _location.confirmHEREPrivacyNoticeException();</code></pre>

 



</div>
`
}</HTMLBlock>
