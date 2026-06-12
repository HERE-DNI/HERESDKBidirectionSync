---
title: "getCustomWarningNotificationDistances abstract method"
slug: "sdk-for-flutter-navigate-warner-warnerengine-getcustomwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getCustomWarningNotificationDistances.html -->


<div>
<h1>getCustomWarningNotificationDistances abstract method</h1></div>

<a href="/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a>
getCustomWarningNotificationDistances(<ol class="parameter-list single-line"> <li>int customWarningType</li>
</ol>)

      

    

<p>Returns the warning notification distances for the specified custom warning type.</p>
<p>Unlike <a href="/sdk-for-flutter-navigate-warner-warnerengine-getwarningnotificationdistances">WarnerEngine.getWarningNotificationDistances</a>, which operates on a <a href="/sdk-for-flutter-navigate-navigation-warningtype">WarningType</a>,
this method targets a specific custom warning category identified by <code>WarnerEngine.getCustomWarningNotificationDistances.customWarningType</code>,
as defined in <a href="/sdk-for-flutter-navigate-warner-customwarning-customwarningtype">CustomWarning.customWarningType</a> and <a href="/sdk-for-flutter-navigate-warner-warning-customwarningtype">Warning.customWarningType</a>.</p>
<ul>
<li><code>customWarningType</code> The identifier of the custom warning type for which the
notification distances are requested.</li>
</ul>
<p>Returns <a href="/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a>. The warning notification distances configured for the given <code>WarnerEngine.getCustomWarningNotificationDistances.customWarningType</code>.
If no distances have been explicitly set for this type, a default
<a href="/sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> value is returned.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WarningNotificationDistances getCustomWarningNotificationDistances(int customWarningType);</code></pre>

 



</div>
`
}</HTMLBlock>
