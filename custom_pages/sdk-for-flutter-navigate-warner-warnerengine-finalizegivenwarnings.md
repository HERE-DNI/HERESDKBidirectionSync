---
title: "finalizeGivenWarnings abstract method"
slug: "sdk-for-flutter-navigate-warner-warnerengine-finalizegivenwarnings"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- finalizeGivenWarnings.html -->


<div>
<h1>finalizeGivenWarnings abstract method</h1></div>

void
finalizeGivenWarnings()

      

    

<p>Marks all currently active warnings as passed (<code>DistanceType.PASSED</code>), notifies all
registered <a href="/sdk-for-flutter-navigate-warner-warninglistener-class">WarningListener</a> instances on the main thread, and then clears these
warnings from their corresponding registries by invoking the appropriate<code>WarningsRegistry.clear&lt;Type&gt;</code> methods.</p>
<p>This method triggers notifications only for enabled warners. Warning processing may
occur asynchronously unless synchronous mode is enabled.</p>
<p><strong>Note</strong>: Although each warning type can also be cleared manually via the respective
<code>WarningsRegistry.clear&lt;Type&gt;()</code> methods, <code>finalizeGivenWarnings()</code> provides a
unified way to flush all active warnings after they have been reported as
passed. If this method is not invoked, warnings will continue to accumulate in the
registry according to the configured warning-generation options.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void finalizeGivenWarnings();</code></pre>

 



</div>
`
}</HTMLBlock>
