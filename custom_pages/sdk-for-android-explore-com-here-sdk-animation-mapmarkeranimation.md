---
title: "MapMarkerAnimation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-animation-mapmarkeranimation"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.animation](sdk-for-android-explore-com-here-sdk-animation-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.animation.MapMarkerAnimation →
com.here.NativeBase → com.here.sdk.animation.MapMarkerAnimation

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapMarkerAnimation</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

An animation that can be applied to the MapMarker object.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

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
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-animation-mapmarkeranimation-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.animation"><code>MapMarkerAnimation.InstantiationErrorCode</code></a></td>
  <td><div class="block">
  Describes a reason for failing to create a MapMarkerAnimation .
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-animation-mapmarkeranimation-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.animation"><code>MapMarkerAnimation.InstantiationException</code></a></td>
  <td><div class="block">
  Thrown when a problem occurs while trying to create a MapMarkerAnimation
  .
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
  <td><pre><code>MapMarkerAnimation(MapItemKeyFrameTrack track)</code></pre></td>
  <td><div class="block">
  Creates an animation of MapMarker based on provided keyframe track.
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

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.animation.MapItemKeyFrameTrack)"
    class="section detail">

    ### MapMarkerAnimation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMarkerAnimation</span><span class="parameters">(@NonNull
    [MapItemKeyFrameTrack](sdk-for-android-explore-com-here-sdk-animation-mapitemkeyframetrack "class in com.here.sdk.animation") track)</span>
    throws
    <span class="exceptions">[MapMarkerAnimation.InstantiationException](sdk-for-android-explore-com-here-sdk-animation-mapmarkeranimation-instantiationexception "class in com.here.sdk.animation")</span>

    </div>

    <div class="block">

    Creates an animation of MapMarker based on provided keyframe track.
    Supports tracks created with MapItemKeyFrameTrack 'moveTo\*'
    methods. For starting the animation see
    MapMarker.startAnimation(com.here.sdk.animation.MapMarkerAnimation,
    com.here.sdk.animation.AnimationListener) .

    </div>

    Parameters:  
    `track` -

    The track holding the keyframes for the animation.

    Throws:  
    [`MapMarkerAnimation.InstantiationException`](sdk-for-android-explore-com-here-sdk-animation-mapmarkeranimation-instantiationexception "class in com.here.sdk.animation")
    -

    If the specified keyframe track cannot be used to create animation
    of a
    [`MapMarker`](sdk-for-android-explore-com-here-sdk-mapview-mapmarker "class in com.here.sdk.mapview").

    </div>

  </div>

</div>

