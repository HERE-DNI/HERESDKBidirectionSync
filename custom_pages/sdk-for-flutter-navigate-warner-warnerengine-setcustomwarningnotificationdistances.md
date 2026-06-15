---
title: "setCustomWarningNotificationDistances abstract method"
slug: "sdk-for-flutter-navigate-warner-warnerengine-setcustomwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setCustomWarningNotificationDistances.html -->


<div>
<h1>setCustomWarningNotificationDistances abstract method</h1></div>

bool
setCustomWarningNotificationDistances(<ol class="parameter-list single-line"> <li>int customWarningType, </li>
<li><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> warningNotificationDistances</li>
</ol>)

      

    

<p>Sets the warning notification distances for the specified custom warning type.</p>
<p>Unlike <a href="sdk-for-flutter-navigate-warner-warnerengine-setwarningnotificationdistances">WarnerEngine.setWarningNotificationDistances</a>, which applies settings to a <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a>,
this method allows configuring notification distances independently for each custom warning
category identified by <code>WarnerEngine.setCustomWarningNotificationDistances.customWarningType</code>, as defined in
<a href="sdk-for-flutter-navigate-warner-customwarning-customwarningtype">CustomWarning.customWarningType</a> and <a href="sdk-for-flutter-navigate-warner-warning-customwarningtype">Warning.customWarningType</a>.</p>
<ul>
<li>
<p><code>customWarningType</code> The identifier of the custom warning type for which the
notification distances should be set.</p>
</li>
<li>
<p><code>warningNotificationDistances</code> The warning notification distances to be applied
for the specified <code>WarnerEngine.setCustomWarningNotificationDistances.customWarningType</code>.</p>
</li>
</ul>
<p>Returns <code>bool</code>. True if the distances were successfully set; false otherwise.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected
behaviors. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool setCustomWarningNotificationDistances(int customWarningType, WarningNotificationDistances warningNotificationDistances);</code></pre>

 



</div>
`
}</HTMLBlock>
