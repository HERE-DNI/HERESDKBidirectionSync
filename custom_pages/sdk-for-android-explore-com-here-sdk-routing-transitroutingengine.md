---
title: "TransitRoutingEngine (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-routing-transitroutingengine"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.routing](sdk-for-android-explore-com-here-sdk-routing-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.routing.TransitRoutingEngine →
com.here.NativeBase → com.here.sdk.routing.TransitRoutingEngine

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TransitRoutingEngine</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Use the TransitRoutingEngine to calculate a public transit route from A
to B with a number of waypoints in between. Route calculation is done
asynchronously and requires an online connection. The resulting route
contains various information such as the polyline, route length in
meters, estimated time to traverse along the route and maneuver data.
Note : Clients need to explicitly call dispose() in order to prevent a
possible, though unlikely, deadlock on destruction.

</div>

</div>

<div class="section summary">

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>TransitRoutingEngine()</code></pre></td>
  <td><div class="block">
  Creates a new instance of this class.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>TransitRoutingEngine(SDKNativeEngine sdkEngine)</code></pre></td>
  <td><div class="block">
  Creates a new instance of TransitRoutingEngine.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-threading-taskhandle"
  title="interface in com.here.sdk.core.threading"><code>TaskHandle</code></a></td>
  <td><pre><code>calculateRoute(TransitWaypoint startingPoint,
   TransitWaypoint destination,
   TransitRouteOptions routeOptions,
   CalculateRouteCallback callback)</code></pre></td>
  <td><div class="block">
  Asynchronously calculates a public transit route from the origin to the
  destination.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>dispose()</code></pre></td>
  <td><div class="block">
  Cancels pending requests and closes the background worker thread.
  </div></td>
  </tr>
  </tbody>
  </table>

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

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### TransitRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TransitRoutingEngine</span>()
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of this class.

    </div>

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="<init>(com.here.sdk.core.engine.SDKNativeEngine)"
    class="section detail">

    ### TransitRoutingEngine

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TransitRoutingEngine</span><span class="parameters">(@NonNull
    [SDKNativeEngine](sdk-for-android-explore-com-here-sdk-core-engine-sdknativeengine "class in com.here.sdk.core.engine") sdkEngine)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new instance of TransitRoutingEngine.

    </div>

    Parameters:  
    `sdkEngine` -

    An SDKEngine instance.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="calculateRoute(com.here.sdk.routing.TransitWaypoint,com.here.sdk.routing.TransitWaypoint,com.here.sdk.routing.TransitRouteOptions,com.here.sdk.routing.CalculateRouteCallback)"
    class="section detail">

    ### calculateRoute

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[TaskHandle](sdk-for-android-explore-com-here-sdk-core-threading-taskhandle "interface in com.here.sdk.core.threading")</span> <span class="element-name">calculateRoute</span><span class="parameters">(@NonNull
    [TransitWaypoint](sdk-for-android-explore-com-here-sdk-routing-transitwaypoint "class in com.here.sdk.routing") startingPoint,
    @NonNull
    [TransitWaypoint](sdk-for-android-explore-com-here-sdk-routing-transitwaypoint "class in com.here.sdk.routing") destination,
    @NonNull
    [TransitRouteOptions](sdk-for-android-explore-com-here-sdk-routing-transitrouteoptions "class in com.here.sdk.routing") routeOptions,
    @NonNull
    [CalculateRouteCallback](sdk-for-android-explore-com-here-sdk-routing-calculateroutecallback "interface in com.here.sdk.routing") callback)</span>

    </div>

    <div class="block">

    Asynchronously calculates a public transit route from the origin to
    the destination.

    </div>

    Parameters:  
    `startingPoint` -

    Position of starting point.

    `destination` -

    Position of destination.

    `routeOptions` -

    Options for public transit route calculation.

    `callback` -

    Callback object that will be invoked after route calculation. It is
    always invoked on the main thread.

    Returns:  
    Handle that will be used to manipulate the execution of the task.

    </div>

  - <div id="dispose()" class="section detail">

    ### dispose

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">dispose</span>()

    </div>

    <div class="block">

    Cancels pending requests and closes the background worker thread.
    Note: This method should be called from main thread.

    </div>

    </div>

  </div>

</div>

