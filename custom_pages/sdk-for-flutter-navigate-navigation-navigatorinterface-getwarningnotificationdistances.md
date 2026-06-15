---
title: "getWarningNotificationDistances abstract method"
slug: "sdk-for-flutter-navigate-navigation-navigatorinterface-getwarningnotificationdistances"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getWarningNotificationDistances.html -->


<div>
<h1>getWarningNotificationDistances abstract method</h1></div>

<a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a>
getWarningNotificationDistances(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a> warningType</li>
</ol>)

      

    

<p>Returns the warning notification distances for the requested warning type.</p>
<p>The return value can be used as the
base for configuring warning notification distances. Configure the relevant attributes of this object according
to your preferences, and then set it by calling <code>setWarningNotificationDistances</code> function with the same
warning type and the modified warning notification distances object.</p>
<ul>
<li><code>warningType</code> The warning type for which the notification distances will be returned.</li>
</ul>
<p>Returns <a href="sdk-for-flutter-navigate-navigation-warningnotificationdistances-class">WarningNotificationDistances</a>. The notification distances for the given warning type.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">WarningNotificationDistances getWarningNotificationDistances(WarningType warningType);</code></pre>

 



</div>
`
}</HTMLBlock>
