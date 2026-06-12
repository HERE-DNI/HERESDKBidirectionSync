---
title: "memoryManagementStrategy property"
slug: "sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-memorymanagementstrategy"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- memoryManagementStrategy.html -->


<div>
<h1>memoryManagementStrategy property</h1></div>

<a href="/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementstrategy">MapContextMemoryManagementStrategy</a>
memoryManagementStrategy
<div class="features">getter/setter pair</div>


<p>The default setting MemoryManagementStrategy.DYNAMIC is suitable for common cases. The map
data cache can adjust dynamically to fit visible data. When the visible data needs extra
memory, it would increase. When it's not needed, it will reduce to a limit which is
calculated internally or by using <a href="/sdk-for-flutter-navigate-mapview-mapcontextmemorymanagementoptions-tilecachememorylimitinkib">MapContextMemoryManagementOptions.tileCacheMemoryLimitInKiB</a> option.
The MemoryManagementStrategy.FIXED would be only useful when there is very
strict memory consumption requirement for the application. It potentially can have
flickering visual artifacts when the map data to be visualized is very large and exceeds
the cache limit.</p>


<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">MapContextMemoryManagementStrategy memoryManagementStrategy;</code></pre>

 



</div>
`
}</HTMLBlock>
