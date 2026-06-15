---
title: "TimeRule constructor"
slug: "sdk-for-flutter-navigate-core-timerule-timerule"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- TimeRule.html -->


<div>
<h1>TimeRule constructor</h1></div>

TimeRule(<ol class="parameter-list single-line"> <li>String timeRule, </li>
<li>int timeZoneOffsetSeconds, </li>
<li>String dstSpec</li>
</ol>)
    

<p>Creates a new instance of this class.</p>
<ul>
<li>
<p><code>timeRule</code> The time rule as a string in ISO 14825 format.</p>
</li>
<li>
<p><code>timeZoneOffsetSeconds</code> The time zone offset in seconds for the location where the time rule applies.</p>
</li>
<li>
<p><code>dstSpec</code> Day saving time specification, as a string in ISO 14825 format, for the location where the time rule applies.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory TimeRule(String timeRule, int timeZoneOffsetSeconds, String dstSpec) =&gt; $prototype.make(timeRule, timeZoneOffsetSeconds, dstSpec);</code></pre>

 



</div>
`
}</HTMLBlock>
