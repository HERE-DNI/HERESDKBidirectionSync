---
title: "EVSearchEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-evsearchengine"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.search.EVSearchEngine
→ com.here.NativeBase → com.here.sdk.search.EVSearchEngine

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

All Implemented Interfaces:  
[`EVSearchInterface`](sdk-for-android-explore-com-here-sdk-search-evsearchinterface "interface in com.here.sdk.search")

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">EVSearchEngine</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")
implements
[EVSearchInterface](sdk-for-android-explore-com-here-sdk-search-evsearchinterface "interface in com.here.sdk.search")</span>

</div>

<div class="block">

The EVSearchEngine API provides detailed information about charging
locations. It requires an online connection to execute the requests. A
licence is required to use this API. Details can be found in HERE EV
Charge Points API v3 - Developer Guide . Note: This is a beta release of
this feature, so there could be a few bugs and unexpected behaviors.
Related APIs may change for new releases without a deprecation process.

</div>

</div>

<div class="section summary">
<div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      EVSearchEngine()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance of this class.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      EVSearchEngine(SDKNativeEngine sdkEngine)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new instance of this class.

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

  [`TaskHandle`](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      search(List<String> ids,
       EVSearchCallback callback)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Performs an asynchronous request for EVChargingLocation instances with
  given Place IDs.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOptions(EVSearchOptions options)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Configures the behavior of EVSearchEngine using the provided input
  options.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>()" class="section detail">

    ### EVSearchEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EVSearchEngine</span>()
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")

    Indicates what went wrong when the instantiation was attempted.

    </div>
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.engine.SDKNativeEngine)"
    class="section detail">

    ### EVSearchEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">EVSearchEngine</span><span class="parameters">(@NonNull
    [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkEngine)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Parameters:  
    `sdkEngine` -

    Instance of an existing SDKEngine.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-setOptions(com.here.sdk.search.EVSearchOptions)"
    class="section detail">

    ### setOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOptions</span><span class="parameters">(@NonNull
    [EVSearchOptions](sdk-for-android-explore-com-here-sdk-search-evsearchoptions "class in com.here.sdk.search") options)</span>

    </div>

    <div class="block">

    Configures the behavior of EVSearchEngine using the provided input
    options.

    </div>

    Parameters:  
    `options` -

    Options used to customize how `EVSearchEngine` behaves.

    </div>
<div id="sdk-for-android-explore-search(java.util.List,com.here.sdk.search.EVSearchCallback)"
    class="section detail">

    ### search

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">search</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> ids,
    @NonNull
    [EVSearchCallback](sdk-for-android-explore-com-here-sdk-search-evsearchcallback "interface in com.here.sdk.search") callback)</span>

    </div>

    <div class="block">

    Performs an asynchronous request for EVChargingLocation instances
    with given Place IDs.

    </div>

    Specified by:  
    [`search`](sdk-for-android-explore-com-here-sdk-search-evsearchinterface#search(java.util.List,com.here.sdk.search.EVSearchCallback)) in
    interface [`EVSearchInterface`](sdk-for-android-explore-com-here-sdk-search-evsearchinterface "interface in com.here.sdk.search")

    Parameters:  
    `ids` -

    List of charging location identifiers.

    `callback` -

    Callback which receives the result on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  </div>

</div>

