---
title: "EVSearchInterface constructor"
slug: "sdk-for-flutter-navigate-search-evsearchinterface-evsearchinterface"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- EVSearchInterface.html -->


<div>
<h1>EVSearchInterface constructor</h1></div>

EVSearchInterface(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-core-threading-taskhandle-class">TaskHandle</a> searchLambda(<ol class="parameter-list single-line"> <li>List&lt;String&gt;, </li>
<li><a href="sdk-for-flutter-navigate-search-evsearchcallback">EVSearchCallback</a> </li>
</ol>)</li>
</ol>)
    

<p>Provides the abstract class for the <code>EVSearchEngine</code>.</p>
<p><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">factory EVSearchInterface(
  TaskHandle Function(List&lt;String&gt;, EVSearchCallback) searchLambda,

) =&gt; EVSearchInterface$Lambdas(
  searchLambda,

);</code></pre>

 



</div>
`
}</HTMLBlock>
