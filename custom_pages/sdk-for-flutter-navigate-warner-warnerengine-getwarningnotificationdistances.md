---
title: "getWarningNotificationDistances abstract method"
slug: "sdk-for-flutter-navigate-warner-warnerengine-getwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getWarningNotificationDistances.html -->


<div>
<h1>getWarningNotificationDistances abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a>
getWarningNotificationDistances(<ol class="parameter-list single-line"> <li><a href="/sdk-for-flutter-navigate-navigation-warningtype">WarningType</a> warningType</li>
</ol>)

      

    

<p>Returns the warning notification distances for the requested warning type.</p>
<p><strong>Note</strong>: <a href="/sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a> is not a valid value for this method.
Use <a href="/sdk-for-flutter-navigate-warner-warnerengine-getcustomwarningnotificationdistances">WarnerEngine.getCustomWarningNotificationDistances</a> to retrieve distances for a specific
custom warning type.</p>
<ul>
<li><code>warningType</code> The warning type for which the notification distances will be returned.
Must not be <a href="/sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a>.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a>. The warning notification distances for the given <code>WarnerEngine.getWarningNotificationDistances.warningType</code>.
If <code>WarnerEngine.getWarningNotificationDistances.warningType</code> is <a href="/sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a>, a default
<a href="/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> value is returned.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WarningNotificationDistances getWarningNotificationDistances(WarningType warningType);</code></pre>

 



</div>
`
}</HTMLBlock>
