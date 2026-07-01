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

<div id="class-description" class="section class-description">

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

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state#distanceToTargetInMeters"
  class="member-name-link"><code>distanceToTargetInMeters</code></a></td>
  <td><div class="block">
  Distance from the camera to the target point in meters.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geoorientation"
  title="class in com.here.sdk.core"><code>GeoOrientation</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state#orientationAtTarget"
  class="member-name-link"><code>orientationAtTarget</code></a></td>
  <td><div class="block">
  Camera's orientation at target point.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state#targetCoordinates"
  class="member-name-link"><code>targetCoordinates</code></a></td>
  <td><div class="block">
  Camera's 'LookAt' target position in geodetic space.
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcamera-state#zoomLevel"
  class="member-name-link"><code>zoomLevel</code></a></td>
  <td><div class="block">
  Zoom level corresponding to the current distance to target.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  <td><pre><code>State(GeoCoordinates targetCoordinates,
   GeoOrientation orientationAtTarget,
   double distanceToTargetInMeters,
   double zoomLevel)</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

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

- <div id="field-detail" class="section field-details">

  - <div id="targetCoordinates" class="section detail">

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

  - <div id="orientationAtTarget" class="section detail">

    ### orientationAtTarget

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoOrientation](sdk-for-android-explore-com-here-sdk-core-geoorientation "class in com.here.sdk.core")</span> <span class="element-name">orientationAtTarget</span>

    </div>

    <div class="block">

    Camera's orientation at target point.

    </div>

    </div>

  - <div id="distanceToTargetInMeters" class="section detail">

    ### distanceToTargetInMeters

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceToTargetInMeters</span>

    </div>

    <div class="block">

    Distance from the camera to the target point in meters.

    </div>

    </div>

  - <div id="zoomLevel" class="section detail">

    ### zoomLevel

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">zoomLevel</span>

    </div>

    <div class="block">

    Zoom level corresponding to the current distance to target.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoOrientation,double,double)"
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

