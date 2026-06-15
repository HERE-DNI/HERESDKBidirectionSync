---
title: "setWarningNotificationDistances abstract method"
slug: "sdk-for-flutter-navigate-warner-warnerengine-setwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setWarningNotificationDistances.html -->


<div>
<h1>setWarningNotificationDistances abstract method</h1></div>

bool
setWarningNotificationDistances(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a> warningType, </li>
<li><a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a> warningNotificationDistances</li>
</ol>)

      

    

<p>Sets the warning notification distances for the specified warning type.</p>
<p><strong>Note</strong>: <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a> is not a valid value for this method.
Use <a href="sdk-for-flutter-navigate-warner-warnerengine-setcustomwarningnotificationdistances">WarnerEngine.setCustomWarningNotificationDistances</a> to configure distances for a specific
custom warning type.</p>
<ul>
<li>
<p><code>warningType</code> The warning type for which the warning notification distances will be set.
Must not be <a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a>.</p>
</li>
<li>
<p><code>warningNotificationDistances</code> The warning notification distances to be set for the specified warning type.</p>
</li>
</ul>
<p>Returns <code>bool</code>. True if the distances were successfully set; false if <code>WarnerEngine.setWarningNotificationDistances.warningType</code> is
<a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType.custom</a> or the options could not be applied.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">bool setWarningNotificationDistances(WarningType warningType, WarningNotificationDistances warningNotificationDistances);</code></pre>

 



</div>
`
}</HTMLBlock>
