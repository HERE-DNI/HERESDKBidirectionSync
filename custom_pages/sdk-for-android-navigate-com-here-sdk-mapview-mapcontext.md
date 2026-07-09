---
title: "MapContext (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mapcontext"
---

<HTMLBlock>{
`
<div className="sdk-for-android-navigate">
<!-- MapContext.html -->






<div className="flex-box">

<div className="flex-content">

<!-- ======== START OF CLASS DATA ======== -->
<div className="header">
<div className="sub-title"><span className="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-package-summary">com.here.sdk.mapview</a></div>

</div>
<div className="inheritance" title="Inheritance Tree"><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">java.lang.Object</a>
<div className="inheritance"><a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">com.here.NativeBase</a>
<div className="inheritance">com.here.sdk.mapview.MapContext</div>
</div>
</div>
<section className="class-description" id="class-description">

<div className="type-signature"><span className="modifiers">public final class </span><span className="element-name type-name-label">MapContext</span>
<span className="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span></div>
<div className="block"><p>MapContext is the rendering engine and the context in which virtual geographic maps get rendered.
 It runs the render loop or offers the means for the user to run a custom one.
 Data sources, assets and virtual maps can be attached to the context. A virtual map can only
 render data from sources attached to the same context.
 The graphics backend to be used by the engine can be choosen by the user or a platform suitable
 one can be automatically selected internally. Only one graphics backend can be active and once
 selected it cannot be changed.</p></div>
</section>
<section className="summary">
<ul className="summary-list">
<!-- ======== NESTED CLASS SUMMARY ======== -->
<li>
<section className="nested-class-summary" id="nested-class-summary">

<div className="caption"><span>Nested Classes</span></div>
<div className="summary-table three-column-summary">



<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-freeresourceseverity" title="enum class in com.here.sdk.mapview">MapContext.FreeResourceSeverity</a></code></div>
<div className="col-last even-row-color">
<div className="block">The severity of a free resource request.</div>
</div>
<div className="col-first odd-row-color"><code>static final class </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview">MapContext.MemoryManagementOptions</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Memory management options.</div>
</div>
<div className="col-first even-row-color"><code>static final class </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-memorymanagementresult" title="class in com.here.sdk.mapview">MapContext.MemoryManagementResult</a></code></div>
<div className="col-last even-row-color">
<div className="block">Memory management result.</div>
</div>
<div className="col-first odd-row-color"><code>static enum </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-memorymanagementresultcode" title="enum class in com.here.sdk.mapview">MapContext.MemoryManagementResultCode</a></code></div>
<div className="col-last odd-row-color">
<div className="block">The memory management result code.</div>
</div>
<div className="col-first even-row-color"><code>static enum </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-memorymanagementstrategy" title="enum class in com.here.sdk.mapview">MapContext.MemoryManagementStrategy</a></code></div>
<div className="col-last even-row-color">
<div className="block">The memory management strategy.</div>
</div>
<div className="col-first odd-row-color"><code>static enum </code></div>
<div className="col-second odd-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-resourcetype" title="enum class in com.here.sdk.mapview">MapContext.ResourceType</a></code></div>
<div className="col-last odd-row-color">
<div className="block">Types of system resources used by <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview"><code>MapContext</code></a> or any of the entities attached to it, like <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a>.</div>
</div>
<div className="col-first even-row-color"><code>static interface </code></div>
<div className="col-second even-row-color"><code><a className="type-name-link" href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-setmemorymanagementoptionscallback" title="interface in com.here.sdk.mapview">MapContext.SetMemoryManagementOptionsCallback</a></code></div>
<div className="col-last even-row-color">
<div className="block">Callback to handle the memory management result.</div>
</div>
</div>
</section>
</li>
<!-- ========== METHOD SUMMARY =========== -->
<li>
<section className="method-summary" id="method-summary">

<div id="method-summary-table">


</div>
<div className="inherited-list">
<h3 id="methods-inherited-from-class-java.lang.Object">Methods inherited from class java.lang.<a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" title="class or interface in java.lang">Object</a></h3>
<code><a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" title="class or interface in java.lang">clone</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" title="class or interface in java.lang">equals</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" title="class or interface in java.lang">finalize</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" title="class or interface in java.lang">getClass</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" title="class or interface in java.lang">hashCode</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" title="class or interface in java.lang">notify</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" title="class or interface in java.lang">notifyAll</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" title="class or interface in java.lang">toString</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" title="class or interface in java.lang">wait</a>, <a className="external-link" href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" title="class or interface in java.lang">wait</a></code></div>
</section>
</li>
</ul>
</section>
<section className="details">
<ul className="details-list">
<!-- ============ METHOD DETAIL ========== -->
<li>
<section className="method-details" id="method-detail">

<ul className="member-list">
<li>
<section className="detail" id="freeResource(com.here.sdk.mapview.MapContext.ResourceType,com.here.sdk.mapview.MapContext.FreeResourceSeverity)">
<h3>freeResource</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">freeResource</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-resourcetype" title="enum class in com.here.sdk.mapview">MapContext.ResourceType</a> type,
 @NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-freeresourceseverity" title="enum class in com.here.sdk.mapview">MapContext.FreeResourceSeverity</a> severity)</span></div>
<div className="block"><p>Frees a system resource held by the <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext" title="class in com.here.sdk.mapview"><code>MapContext</code></a> and all entities attached to it, like <a href="sdk-for-android-navigate-com-here-sdk-mapview-heremap" title="class in com.here.sdk.mapview"><code>HereMap</code></a>.
 This function is intended for use when a system resource availability becomes low.
 For example, some memory can be freed when the application transitions to the background state.</p></div>
<dl className="notes">
<dt>Parameters:</dt>
<dd><code>type</code> - <p>Type of resource to be freed.</p></dd>
<dd><code>severity</code> - <p>Severity of the request.</p></dd>
</dl>
</section>
</li>
<li>
<section className="detail" id="getMemoryManagementOptions()">
<h3>getMemoryManagementOptions</h3>
<div className="member-signature"><span className="annotations">@NonNull
</span><span className="modifiers">public</span> <span className="return-type"><a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview">MapContext.MemoryManagementOptions</a></span> <span className="element-name">getMemoryManagementOptions</span>()</div>
<dl className="notes">
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
<section className="detail" id="setMemoryManagementOptions(com.here.sdk.mapview.MapContext.MemoryManagementOptions,com.here.sdk.mapview.MapContext.SetMemoryManagementOptionsCallback)">
<h3>setMemoryManagementOptions</h3>
<div className="member-signature"><span className="modifiers">public</span> <span className="return-type">void</span> <span className="element-name">setMemoryManagementOptions</span><wbr/><span className="parameters">(@NonNull
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview">MapContext.MemoryManagementOptions</a> memoryManagementOptions,
 @Nullable
 <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-setmemorymanagementoptionscallback" title="interface in com.here.sdk.mapview">MapContext.SetMemoryManagementOptionsCallback</a> callback)</span></div>
<div className="block"><p>Sets memory management options for controlling tile cache and video memory usage.
 In <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapcontext-memorymanagementoptions" title="class in com.here.sdk.mapview"><code>MapContext.MemoryManagementOptions</code></a> optional parameters with <code>null</code>
 or non positive values will be ignored, preserving their existing settings.
 Note: This is a beta release of this feature, so there could be a few bugs and unexpected
 behavior. Related APIs may change for new releases without a deprecation process.</p></div>
<dl className="notes">
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
