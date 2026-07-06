---
title: "MapCamera.State (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.MapCamera.State

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[MapCamera](sdk-for-android-explore-com-here-sdk-mapview-mapcamera "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapCamera.State</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Encapsulates state of the camera.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `double`

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state#distanceToTargetInMeters"
  class="member-name-link"><code>distanceToTargetInMeters</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Distance from the camera to the target point in meters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  [`GeoOrientation`](sdk-for-android-explore-com-here-sdk-core-geoorientation "class in com.here.sdk.core")

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state#orientationAtTarget"
  class="member-name-link"><code>orientationAtTarget</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Camera's orientation at target point.

  </div>

  </div>

  <div class="col-first even-row-color">

  [`GeoCoordinates`](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state#targetCoordinates"
  class="member-name-link"><code>targetCoordinates</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Camera's 'LookAt' target position in geodetic space.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `double`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state#zoomLevel"
  class="member-name-link"><code>zoomLevel</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Zoom level corresponding to the current distance to target.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
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

      State(GeoCoordinates targetCoordinates,
       GeoOrientation orientationAtTarget,
       double distanceToTargetInMeters,
       double zoomLevel)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

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

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-targetCoordinates"
    class="section detail">

    ### targetCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">targetCoordinates</span>

    </div>

    <div class="block">

    Camera's 'LookAt' target position in geodetic space. Note: The
    altitude of the target point is ignored. Any subsequent camera
    updates and animations will consider the target point as being
    located on the ground.

    </div>

    </div>

  - <div id="sdk-for-android-explore-orientationAtTarget"
    class="section detail">

    ### orientationAtTarget

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoOrientation](sdk-for-android-explore-com-here-sdk-core-geoorientation "class in com.here.sdk.core")</span> <span class="element-name">orientationAtTarget</span>

    </div>

    <div class="block">

    Camera's orientation at target point.

    </div>

    </div>

  - <div id="sdk-for-android-explore-distanceToTargetInMeters"
    class="section detail">

    ### distanceToTargetInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToTargetInMeters</span>

    </div>

    <div class="block">

    Distance from the camera to the target point in meters.

    </div>

    </div>

  - <div id="sdk-for-android-explore-zoomLevel" class="section detail">

    ### zoomLevel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">zoomLevel</span>

    </div>

    <div class="block">

    Zoom level corresponding to the current distance to target.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientation,double,double)"
    class="section detail">

    ### State

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">State</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") targetCoordinates,
    @NonNull
    [GeoOrientation](sdk-for-android-explore-com-here-sdk-core-geoorientation "class in com.here.sdk.core") orientationAtTarget,
    double distanceToTargetInMeters, double zoomLevel)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `targetCoordinates` -

    Camera's 'LookAt' target position in geodetic space. Note: The
    altitude of the target point is ignored. Any subsequent camera
    updates and animations will consider the target point as being
    located on the ground.

    `orientationAtTarget` -

    Camera's orientation at target point.

    `distanceToTargetInMeters` -

    Distance from the camera to the target point in meters.

    `zoomLevel` -

    Zoom level corresponding to the current distance to target.

    </div>

  </div>

</div>

