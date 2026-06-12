---
title: "setEnabledWarnings abstract method"
slug: "sdk-for-flutter-navigate-warner-warnerengine-setenabledwarnings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setEnabledWarnings.html -->


<div>
<h1>setEnabledWarnings abstract method</h1></div>

void
setEnabledWarnings(<ol class="parameter-list single-line"> <li>List&lt;<a href="/sdk-for-flutter-navigate-navigation-warningtype">WarningType</a>&gt; warningTypes</li>
</ol>)

      

    

<p>Replaces the current set of enabled warning types with the provided list.</p>
<p>After this call, the engine will monitor and generate warnings
only for types included in <code>WarnerEngine.setEnabledWarnings.warningTypes</code>.</p>
<ul>
<li><code>warningTypes</code> The complete new set of warning types the engine should track.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setEnabledWarnings(List&lt;WarningType&gt; warningTypes);</code></pre>

 



</div>
`
}</HTMLBlock>
