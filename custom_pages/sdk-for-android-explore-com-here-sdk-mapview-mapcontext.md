---
title: "MapContext (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcontext"
---

<HTMLBlock>{
`
<div class="sdk-for-android">
<!-- MapContext.html -->






<div class="flex-box">

<div class="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div class="header">
<div class="sub-title"><span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-package-summary">com.here.sdk.mapview</a></div>

</div>
<div class="inheritance" title="Inheritance Tree"><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div class="inheritance"><a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div class="inheritance">com.here.sdk.mapview.MapContext</div>
</div>
</div>
<section class="class-description" id="class-description">

<div class="type-signature"><span class="modifiers">public final class </span><span class="element-name type-name-label">MapContext</span>
<span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div class="block"><p>MapContext is the rendering engine and the context in which virtual geographic maps get rendered.
 It runs the render loop or offers the means for the user to run a custom one.
 Data sources, assets and virtual maps can be attached to the context. A virtual map can only
 render data from sources attached to the same context.
 The graphics backend to be used by the engine can be choosen by the user or a platform suitable
 one can be automatically selected internally. Only one graphics backend can be active and once
 selected it cannot be changed.</p></div>
</section>
<section class="summary">
<ul class="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section class="nested-class-summary" id="nested-class-summary">

<div class="caption"><span>Nested Classes</span></div>
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Class</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-freeresourceseverity" title="enum class in com.here.sdk.mapview">MapContext.FreeResourceSeverity</a></code></div>
<div class="col-last even-row-color">
<div class="block">The severity of a free resource request.</div>
</div>
<div class="col-first odd-row-color"><code>static final class </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview">MapContext.MemoryManagementOptions</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Memory management options.</div>
</div>
<div class="col-first even-row-color"><code>static final class </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresult" title="class in com.here.sdk.mapview">MapContext.MemoryManagementResult</a></code></div>
<div class="col-last even-row-color">
<div class="block">Memory management result.</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode" title="enum class in com.here.sdk.mapview">MapContext.MemoryManagementResultCode</a></code></div>
<div class="col-last odd-row-color">
<div class="block">The memory management result code.</div>
</div>
<div class="col-first even-row-color"><code>static enum </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementstrategy" title="enum class in com.here.sdk.mapview">MapContext.MemoryManagementStrategy</a></code></div>
<div class="col-last even-row-color">
<div class="block">The memory management strategy.</div>
</div>
<div class="col-first odd-row-color"><code>static enum </code></div>
<div class="col-second odd-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-resourcetype" title="enum class in com.here.sdk.mapview">MapContext.ResourceType</a></code></div>
<div class="col-last odd-row-color">
<div class="block">Types of system resources used by <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview"><code>MapContext</code></a> or any of the entities attached to it, like <a href="sdk-for-android-explore-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a>.</div>
</div>
<div class="col-first even-row-color"><code>static interface </code></div>
<div class="col-second even-row-color"><code><a class="type-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-setmemorymanagementoptionscallback" title="interface in com.here.sdk.mapview">MapContext.SetMemoryManagementOptionsCallback</a></code></div>
<div class="col-last even-row-color">
<div class="block">Callback to handle the memory management result.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section class="method-summary" id="method-summary">

<div id="method-summary-table">
<div aria-orientation="horizontal" class="table-tabs" role="tablist"><button aria-controls="method-summary-table.tabpanel" aria-selected="true" class="active-table-tab" id="method-summary-table-tab0" onclick="show('method-summary-table', 'method-summary-table', 3)" onkeydown="switchTab(event)" role="tab" tabindex="0">All Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab2" onclick="show('method-summary-table', 'method-summary-table-tab2', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Instance Methods</button><button aria-controls="method-summary-table.tabpanel" aria-selected="false" class="table-tab" id="method-summary-table-tab4" onclick="show('method-summary-table', 'method-summary-table-tab4', 3)" onkeydown="switchTab(event)" role="tab" tabindex="-1">Concrete Methods</button></div>
<div aria-labelledby="method-summary-table-tab0" id="method-summary-table.tabpanel" role="tabpanel">
<div class="summary-table three-column-summary">
<div class="table-header col-first">Modifier and Type</div>
<div class="table-header col-second">Method</div>
<div class="table-header col-last">Description</div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext#freeResource(com.here.sdk.mapview.MapContext.ResourceType,com.here.sdk.mapview.MapContext.FreeResourceSeverity)">freeResource</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-resourcetype" title="enum class in com.here.sdk.mapview">MapContext.ResourceType</a> type,
 <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-freeresourceseverity" title="enum class in com.here.sdk.mapview">MapContext.FreeResourceSeverity</a> severity)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Frees a system resource held by the <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview"><code>MapContext</code></a> and all entities attached to it, like <a href="sdk-for-android-explore-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a>.</div>
</div>
<div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview">MapContext.MemoryManagementOptions</a></code></div>
<div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext#getMemoryManagementOptions()">getMemoryManagementOptions</a>()</code></div>
<div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"> </div>
<div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code>void</code></div>
<div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4"><code><a class="member-name-link" href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext#setMemoryManagementOptions(com.here.sdk.mapview.MapContext.MemoryManagementOptions,com.here.sdk.mapview.MapContext.SetMemoryManagementOptionsCallback)">setMemoryManagementOptions</a><wbr/>(<a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview">MapContext.MemoryManagementOptions</a> memoryManagementOptions,
 <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-setmemorymanagementoptionscallback" title="interface in com.here.sdk.mapview">MapContext.SetMemoryManagementOptionsCallback</a> callback)</code></div>
<div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">
<div class="block">Sets memory management options for controlling tile cache and video memory usage.</div>
</div>
</div>
</div>
</div>
<div class="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a class="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section class="details">
<ul class="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section class="method-details" id="method-detail">

<ul class="member-list">
<li>
<section class="detail" id="freeResource(com.here.sdk.mapview.MapContext.ResourceType,com.here.sdk.mapview.MapContext.FreeResourceSeverity)">
<h3>freeResource</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">freeResource</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-resourcetype" title="enum class in com.here.sdk.mapview">MapContext.ResourceType</a> type,
 @NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-freeresourceseverity" title="enum class in com.here.sdk.mapview">MapContext.FreeResourceSeverity</a> severity)</span></div>
<div class="block"><p>Frees a system resource held by the <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview"><code>MapContext</code></a> and all entities attached to it, like <a href="sdk-for-android-explore-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a>.
 This function is intended for use when a system resource availability becomes low.
 For example, some memory can be freed when the application transitions to the background state.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - <p>Type of resource to be freed.</p></dd>
<dd><code>severity</code> - <p>Severity of the request.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="getMemoryManagementOptions()">
<h3>getMemoryManagementOptions</h3>
<div class="member-signature"><span class="annotations">@NonNull
</span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview">MapContext.MemoryManagementOptions</a></span> <span class="element-name">getMemoryManagementOptions</span>()</div>
<dl class="notes">
<dt>Returns:</dt>
<dd><p>Gets the current memory management options.
     Returns the actual applied memory limits. If the underlying system limits exceed
     int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value is clamped to int32_t max.
     Note: This is a beta release of this feature, so there could be a few bugs and unexpected
     behavior. Related APIs may change for new releases without a deprecation process.</p></dd>
</dl>
</section>
</li>
<li>
<section class="detail" id="setMemoryManagementOptions(com.here.sdk.mapview.MapContext.MemoryManagementOptions,com.here.sdk.mapview.MapContext.SetMemoryManagementOptionsCallback)">
<h3>setMemoryManagementOptions</h3>
<div class="member-signature"><span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMemoryManagementOptions</span><wbr/><span class="parameters">(@NonNull
 <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview">MapContext.MemoryManagementOptions</a> memoryManagementOptions,
 @Nullable
 <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-setmemorymanagementoptionscallback" title="interface in com.here.sdk.mapview">MapContext.SetMemoryManagementOptionsCallback</a> callback)</span></div>
<div class="block"><p>Sets memory management options for controlling tile cache and video memory usage.
 In <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview"><code>MapContext.MemoryManagementOptions</code></a> optional parameters with <code>null</code>
 or non positive values will be ignored, preserving their existing settings.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl class="notes">
<dt>Parameters:</dt>
<dd><code>memoryManagementOptions</code> - <p>The memory management options to set.</p></dd>
<dd><code>callback</code> - <p>Optional callback used upon
     completion to pass the return value to the caller.
     The callback is called on the main thread.</p></dd>
</dl>
</section>
</li>
</ul>
</section>
</li>
</ul>
</section>
<!-- ========= END OF CLASS DATA ========= -->

</div>
</div>



</div>
`
}</HTMLBlock>
