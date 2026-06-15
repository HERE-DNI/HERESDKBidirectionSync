---
title: "addEnabledWarnings abstract method"
slug: "sdk-for-flutter-navigate-warner-warnerengine-addenabledwarnings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- addEnabledWarnings.html -->


<div>
<h1>addEnabledWarnings abstract method</h1></div>

void
addEnabledWarnings(<ol class="parameter-list single-line"> <li>List&lt;<a href="sdk-for-flutter-navigate-navigation-warningtype">WarningType</a>&gt; warningTypes</li>
</ol>)

      

    

<p>Adds the given warning types to the set of warnings monitored by the engine.</p>
<p>After this call, the engine will begin generating warnings for all
types included in <code>WarnerEngine.addEnabledWarnings.warningTypes</code>, in addition to those that are already enabled.</p>
<ul>
<li><code>warningTypes</code> Warning types to be added to the engine's active monitoring set.</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void addEnabledWarnings(List&lt;WarningType&gt; warningTypes);</code></pre>

 



</div>
`
}</HTMLBlock>
