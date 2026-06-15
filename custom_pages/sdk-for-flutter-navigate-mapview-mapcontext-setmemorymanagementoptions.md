---
title: "setMemoryManagementOptions abstract method"
slug: "sdk-for-flutter-navigate-mapview-mapcontext-setmemorymanagementoptions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- setMemoryManagementOptions.html -->


<div>
<h1>setMemoryManagementOptions abstract method</h1></div>

void
setMemoryManagementOptions(<ol class="parameter-list single-line"> <li><a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a> memoryManagementOptions, </li>
<li><a href="sdk-for-flutter-navigate-mapview-mapcontextsetmemorymanagementoptionscallback">MapContextSetMemoryManagementOptionsCallback</a>? callback</li>
</ol>)

      

    

<p>Sets memory management options for controlling tile cache and video memory usage.</p>
<p>In <a href="sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-class">MapContextMemoryManagementOptions</a> optional parameters with <code>null</code>
or non positive values will be ignored, preserving their existing settings.</p>
<p>Note: This is a beta release of this feature, so there could be a few bugs and unexpected
behavior. Related APIs may change for new releases without a deprecation process.</p>
<ul>
<li>
<p><code>memoryManagementOptions</code> The memory management options to set.</p>
</li>
<li>
<p><code>callback</code> Optional callback used upon
completion to pass the return value to the caller.
The callback is called from an arbitrary thread.</p>
</li>
</ul>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">void setMemoryManagementOptions(MapContextMemoryManagementOptions memoryManagementOptions, MapContextSetMemoryManagementOptionsCallback? callback);</code></pre>

 



</div>
`
}</HTMLBlock>
