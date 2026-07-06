---
title: "MapContext (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcontext"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.MapContext →
com.here.NativeBase → com.here.sdk.mapview.MapContext

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapContext</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

MapContext is the rendering engine and the context in which virtual
geographic maps get rendered. It runs the render loop or offers the
means for the user to run a custom one. Data sources, assets and virtual
maps can be attached to the context. A virtual map can only render data
from sources attached to the same context. The graphics backend to be
used by the engine can be choosen by the user or a platform suitable one
can be automatically selected internally. Only one graphics backend can
be active and once selected it cannot be changed.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-freeresourceseverity" class="type-name-link" title="enum class in com.here.sdk.mapview"><code>MapContext.FreeResourceSeverity</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The severity of a free resource request.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions" class="type-name-link" title="class in com.here.sdk.mapview"><code>MapContext.MemoryManagementOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Memory management options.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresult" class="type-name-link" title="class in com.here.sdk.mapview"><code>MapContext.MemoryManagementResult</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Memory management result.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static enum `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementresultcode" class="type-name-link" title="enum class in com.here.sdk.mapview"><code>MapContext.MemoryManagementResultCode</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The memory management result code.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementstrategy" class="type-name-link" title="enum class in com.here.sdk.mapview"><code>MapContext.MemoryManagementStrategy</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The memory management strategy.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static enum `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-resourcetype" class="type-name-link" title="enum class in com.here.sdk.mapview"><code>MapContext.ResourceType</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Types of system resources used by MapContext or any of the entities
  attached to it, like HereMap .

  </div>

  </div>

  <div class="col-first even-row-color">

  `static interface `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-mapcontext-setmemorymanagementoptionscallback" class="type-name-link" title="interface in com.here.sdk.mapview"><code>MapContext.SetMemoryManagementOptionsCallback</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Callback to handle the memory management result.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      freeResource(MapContext.ResourceType type,
       MapContext.FreeResourceSeverity severity)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Frees a system resource held by the MapContext and all entities
  attached to it, like HereMap .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapContext.MemoryManagementOptions`](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMemoryManagementOptions()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMemoryManagementOptions(MapContext.MemoryManagementOptions memoryManagementOptions,
       MapContext.SetMemoryManagementOptionsCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets memory management options for controlling tile cache and video
  memory usage.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-freeResource(com.here.sdk.mapview.MapContext.ResourceType,com.here.sdk.mapview.MapContext.FreeResourceSeverity)"
    class="section detail">

    ### freeResource

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">freeResource</span><span class="parameters">(@NonNull
    [MapContext.ResourceType](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-resourcetype "enum class in com.here.sdk.mapview") type,
    @NonNull
    [MapContext.FreeResourceSeverity](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-freeresourceseverity "enum class in com.here.sdk.mapview") severity)</span>

    </div>

    <div class="block">

    Frees a system resource held by the MapContext and all entities
    attached to it, like HereMap . This function is intended for use
    when a system resource availability becomes low. For example, some
    memory can be freed when the application transitions to the
    background state.

    </div>

    Parameters:  
    `type` -

    Type of resource to be freed.

    `severity` -

    Severity of the request.

    </div>
<div id="sdk-for-android-explore-getMemoryManagementOptions()"
    class="section detail">

    ### getMemoryManagementOptions

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapContext.MemoryManagementOptions](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions "class in com.here.sdk.mapview")</span> <span class="element-name">getMemoryManagementOptions</span>()

    </div>

    Returns:  
    Gets the current memory management options. Returns the actual
    applied memory limits. If the underlying system limits exceed
    int32_t max value (2,147,483,647 KiB or ~2 TiB), the returned value
    is clamped to int32_t max. Note: This is a beta release of this
    feature, so there could be a few bugs and unexpected behavior.
    Related APIs may change for new releases without a deprecation
    process.

    </div>
<div id="sdk-for-android-explore-setMemoryManagementOptions(com.here.sdk.mapview.MapContext.MemoryManagementOptions,com.here.sdk.mapview.MapContext.SetMemoryManagementOptionsCallback)"
    class="section detail">

    ### setMemoryManagementOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMemoryManagementOptions</span><span class="parameters">(@NonNull
    [MapContext.MemoryManagementOptions](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-memorymanagementoptions "class in com.here.sdk.mapview") memoryManagementOptions,
    @Nullable
    [MapContext.SetMemoryManagementOptionsCallback](sdk-for-android-explore-com-here-sdk-mapview-mapcontext-setmemorymanagementoptionscallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Sets memory management options for controlling tile cache and video
    memory usage. In MapContext.MemoryManagementOptions optional
    parameters with null or non positive values will be ignored,
    preserving their existing settings. Note: This is a beta release of
    this feature, so there could be a few bugs and unexpected behavior.
    Related APIs may change for new releases without a deprecation
    process.

    </div>

    Parameters:  
    `memoryManagementOptions` -

    The memory management options to set.

    `callback` -

    Optional callback used upon completion to pass the return value to
    the caller. The callback is called on the main thread.

    </div>

  </div>

</div>

