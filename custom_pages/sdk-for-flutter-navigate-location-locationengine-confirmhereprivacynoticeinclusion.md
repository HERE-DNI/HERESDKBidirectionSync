---
title: "confirmHEREPrivacyNoticeInclusion method"
slug: "sdk-for-flutter-navigate-location-locationengine-confirmhereprivacynoticeinclusion"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- confirmHEREPrivacyNoticeInclusion.html -->


<div>
<h1>confirmHEREPrivacyNoticeInclusion method</h1></div>

<a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus</a>
confirmHEREPrivacyNoticeInclusion()

      <div class="features">override</div>


<p>On Android devices it is the responsibility of the application developer to ensure that
the application user is informed about the collection of characteristic information
regarding nearby mobile and Wi-Fi network signals. Additionally, a link to the related
<a href="https://legal.here.com/here-network-positioning-via-sdk">HERE Privacy Notice</a>
must be made available to the user.</p>
<p>This information can be included in the application's Terms &amp; Conditions,
or Privacy Policy, or otherwise made accessible to the user.</p>
<p><strong>Example text for informing users about data collection:</strong></p>
<blockquote>
<p>"This application uses location services provided by HERE Technologies.
To maintain, improve, and provide these services, HERE Technologies occasionally collects
characteristic information about nearby mobile and Wi-Fi network signals.
For more information, please refer to the HERE Privacy Notice at:
<a href="https://legal.here.com/here-network-positioning-via-sdk">https://legal.here.com/here-network-positioning-via-sdk</a>"</p>
</blockquote>
<p><strong>Note:</strong> By calling this method, the application developer confirms that
this information is made available to the end user.</p>
<p>For example, it is sufficient to inform users once that using the app requires
acceptance of its terms (if any). Then, in the terms include the
above mentioned data collection information and a link to the related HERE Privacy Notice.
The user is not required to open the terms to acknowledge the data collection details.
The "Positioning" example app on <a href="https://github.com/heremaps/here-sdk-examples">GitHub</a>
provides an example of this.</p>
<p>When the above criteria are met, it is recommended to silently execute this
method each time before starting the <code>LocationEngine</code>, as failure to do so
will result in the engine being non-functional.</p>
<p>Returns:</p>
<ul>
<li>Immediately returns with <code>ConfirmationStatus.OK</code>.</li>
</ul>
<p>On iOS devices this method does nothing and <a href="sdk-for-flutter-navigate-location-confirmationstatus">ConfirmationStatus.ok</a> is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">ConfirmationStatus confirmHEREPrivacyNoticeInclusion() =&gt;
    _location.confirmHEREPrivacyNoticeInclusion();</code></pre>

 



</div>
`
}</HTMLBlock>
