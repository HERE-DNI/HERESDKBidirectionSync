---
title: "getMemoryManagementOptions abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapcontext-getmemorymanagementoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getMemoryManagementOptions.html -->


<div>
<h1>getMemoryManagementOptions abstract method</h1></div>

<a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a>
getMemoryManagementOptions()

      

    

<p>Returns <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a>. Gets the current memory management options.
Returns the actual applied memory limits. If the underlying system limits exceed
int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to int32_t max.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapContextMemoryManagementOptions getMemoryManagementOptions();</code></pre>

 



</div>
`
}</HTMLBlock>
