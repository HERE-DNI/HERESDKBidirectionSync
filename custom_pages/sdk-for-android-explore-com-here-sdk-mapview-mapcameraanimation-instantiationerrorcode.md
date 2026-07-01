---
title: "MapCameraAnimation.InstantiationErrorCode (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
java.lang.Enum<MapCameraAnimation.InstantiationErrorCode>com.here.sdk.mapview.MapCameraAnimation.InstantiationErrorCode
→ java.lang.Enum → MapCameraAnimation.InstantiationErrorCode →
com.here.sdk.mapview.MapCameraAnimation.InstantiationErrorCode

</div>

<div id="class-description" class="section class-description">

All Implemented Interfaces:  
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html"
class="external-link"
title="class or interface in java.io"><code>Serializable</code></a>, <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html"
class="external-link"
title="class or interface in java.lang"><code>Comparable</code></a>`<`[`MapCameraAnimation.InstantiationErrorCode`](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")`>`,
<a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html"
class="external-link"
title="class or interface in java.lang.constant"><code>Constable</code></a>

<!-- -->

Enclosing class:  
[MapCameraAnimation](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static enum
</span><span class="element-name type-name-label">MapCameraAnimation.InstantiationErrorCode</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
class="external-link" title="class or interface in java.lang">Enum</a><[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")></span>

</div>

<div class="block">

Describes a reason for failing to create a multi-track
MapCameraAnimation .

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>` extends `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link"
  title="class or interface in java.lang"><code>Enum</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html"
  class="external-link"
  title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="enum-constant-summary" class="section constants-summary">

  <div class="caption">

  Enum Constants

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Enum Constant</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_ORIENTATION_TRACK"
  class="member-name-link"><code>CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_ORIENTATION_TRACK</code></a></td>
  <td><div class="block">
  Camera's look-at distance is already modified by an earlier track that
  modifies camera's orientation.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_POSITION_TRACK"
  class="member-name-link"><code>CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_POSITION_TRACK</code></a></td>
  <td><div class="block">
  Camera's look-at distance is already modified by an earlier track that
  modifies camera's position.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_ORIENTATION_TRACK"
  class="member-name-link"><code>CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_ORIENTATION_TRACK</code></a></td>
  <td><div class="block">
  Camera's look-at orientation is already modified by an earlier track
  that modifies camera's orientation.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_POSITION_TRACK"
  class="member-name-link"><code>CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_POSITION_TRACK</code></a></td>
  <td><div class="block">
  Camera's look-at orientation is already modified by an earlier track
  that modifies camera's position.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_ORIENTATION_TRACK"
  class="member-name-link"><code>CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_ORIENTATION_TRACK</code></a></td>
  <td><div class="block">
  Camera's look-at target is already modified by an earlier track that
  modifies camera's orientation.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_POSITION_TRACK"
  class="member-name-link"><code>CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_POSITION_TRACK</code></a></td>
  <td><div class="block">
  Camera's look-at target is already modified by an earlier track that
  modifies camera's position.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK"
  class="member-name-link"><code>CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK</code></a></td>
  <td><div class="block">
  Camera's orientation is already modified by an earlier track that
  modifies camera's look-at distance.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK"
  class="member-name-link"><code>CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK</code></a></td>
  <td><div class="block">
  Camera's orientation is already modified by an earlier track that
  modifies camera's look-at orientation.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK"
  class="member-name-link"><code>CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK</code></a></td>
  <td><div class="block">
  Camera's position is already modified by an earlier track that modifies
  camera's look-at distance.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK"
  class="member-name-link"><code>CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK</code></a></td>
  <td><div class="block">
  Camera's position is already modified by an earlier track that modifies
  camera's look-at orientation.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_TARGET_TRACK"
  class="member-name-link"><code>CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_TARGET_TRACK</code></a></td>
  <td><div class="block">
  Camera's position is already modified by an earlier track that modifies
  camera's look-at target.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#EMPTY_TRACK_LIST"
  class="member-name-link"><code>EMPTY_TRACK_LIST</code></a></td>
  <td><div class="block">
  List of keyframe tracks is empty.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#MULTIPLE_CAMERA_FIELD_OF_VIEW_TRACKS"
  class="member-name-link"><code>MULTIPLE_CAMERA_FIELD_OF_VIEW_TRACKS</code></a></td>
  <td><div class="block">
  List of keyframe tracks contains multiple camera field-of-view tracks.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#MULTIPLE_CAMERA_FOCAL_LENGTH_TRACKS"
  class="member-name-link"><code>MULTIPLE_CAMERA_FOCAL_LENGTH_TRACKS</code></a></td>
  <td><div class="block">
  List of keyframe tracks contains multiple camera focal length tracks.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#MULTIPLE_CAMERA_LOOKAT_DISTANCE_TRACKS"
  class="member-name-link"><code>MULTIPLE_CAMERA_LOOKAT_DISTANCE_TRACKS</code></a></td>
  <td><div class="block">
  List of keyframe tracks contains multiple camera look-at distance
  tracks.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#MULTIPLE_CAMERA_LOOKAT_ORIENTATION_TRACKS"
  class="member-name-link"><code>MULTIPLE_CAMERA_LOOKAT_ORIENTATION_TRACKS</code></a></td>
  <td><div class="block">
  List of keyframe tracks contains multiple camera look-at orientation
  tracks.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#MULTIPLE_CAMERA_LOOKAT_TARGET_TRACKS"
  class="member-name-link"><code>MULTIPLE_CAMERA_LOOKAT_TARGET_TRACKS</code></a></td>
  <td><div class="block">
  List of keyframe tracks contains multiple camera look-at target tracks.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#MULTIPLE_CAMERA_ORIENTATION_TRACKS"
  class="member-name-link"><code>MULTIPLE_CAMERA_ORIENTATION_TRACKS</code></a></td>
  <td><div class="block">
  List of keyframe tracks contains multiple camera orientation tracks.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#MULTIPLE_CAMERA_POSITION_TRACKS"
  class="member-name-link"><code>MULTIPLE_CAMERA_POSITION_TRACKS</code></a></td>
  <td><div class="block">
  List of keyframe tracks contains multiple camera position tracks.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode#MULTIPLE_CAMERA_PRINCIPAL_POINT_TRACKS"
  class="member-name-link"><code>MULTIPLE_CAMERA_PRINCIPAL_POINT_TRACKS</code></a></td>
  <td><div class="block">
  List of keyframe tracks contains multiple camera principal point tracks.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
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
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview"><code>MapCameraAnimation.InstantiationErrorCode</code></a></td>
  <td><pre><code>valueOf(String name)</code></pre></td>
  <td><div class="block">
  Returns the enum constant of this class with the specified name.
  </div></td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode"
  title="enum class in com.here.sdk.mapview"><code>MapCameraAnimation.InstantiationErrorCode</code></a><code>[]</code></td>
  <td><pre><code>values()</code></pre></td>
  <td><div class="block">
  Returns an array containing the constants of this enum class, in the
  order they are declared.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html"
  class="external-link" title="class or interface in java.lang">Enum</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)"
  class="external-link"
  title="class or interface in java.lang"><code>compareTo</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()"
  class="external-link"
  title="class or interface in java.lang"><code>describeConstable</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getDeclaringClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()"
  class="external-link"
  title="class or interface in java.lang"><code>name</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()"
  class="external-link"
  title="class or interface in java.lang"><code>ordinal</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)"
  class="external-link"
  title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
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

- <div id="enum-constant-detail" class="section constant-details">

  - <div id="EMPTY_TRACK_LIST" class="section detail">

    ### EMPTY_TRACK_LIST

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">EMPTY_TRACK_LIST</span>

    </div>

    <div class="block">

    List of keyframe tracks is empty.

    </div>

    </div>

  - <div id="MULTIPLE_CAMERA_POSITION_TRACKS" class="section detail">

    ### MULTIPLE_CAMERA_POSITION_TRACKS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">MULTIPLE_CAMERA_POSITION_TRACKS</span>

    </div>

    <div class="block">

    List of keyframe tracks contains multiple camera position tracks.

    </div>

    </div>

  - <div id="CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_TARGET_TRACK"
    class="section detail">

    ### CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_TARGET_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_TARGET_TRACK</span>

    </div>

    <div class="block">

    Camera's position is already modified by an earlier track that
    modifies camera's look-at target.

    </div>

    </div>

  - <div id="CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK"
    class="section detail">

    ### CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK</span>

    </div>

    <div class="block">

    Camera's position is already modified by an earlier track that
    modifies camera's look-at orientation.

    </div>

    </div>

  - <div id="CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK"
    class="section detail">

    ### CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_POSITION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK</span>

    </div>

    <div class="block">

    Camera's position is already modified by an earlier track that
    modifies camera's look-at distance.

    </div>

    </div>

  - <div id="MULTIPLE_CAMERA_ORIENTATION_TRACKS" class="section detail">

    ### MULTIPLE_CAMERA_ORIENTATION_TRACKS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">MULTIPLE_CAMERA_ORIENTATION_TRACKS</span>

    </div>

    <div class="block">

    List of keyframe tracks contains multiple camera orientation tracks.

    </div>

    </div>

  - <div id="CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK"
    class="section detail">

    ### CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_ORIENTATION_TRACK</span>

    </div>

    <div class="block">

    Camera's orientation is already modified by an earlier track that
    modifies camera's look-at orientation.

    </div>

    </div>

  - <div id="CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK"
    class="section detail">

    ### CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_ORIENTATION_MODIFIED_BY_CAMERA_LOOKAT_DISTANCE_TRACK</span>

    </div>

    <div class="block">

    Camera's orientation is already modified by an earlier track that
    modifies camera's look-at distance.

    </div>

    </div>

  - <div id="MULTIPLE_CAMERA_LOOKAT_TARGET_TRACKS"
    class="section detail">

    ### MULTIPLE_CAMERA_LOOKAT_TARGET_TRACKS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">MULTIPLE_CAMERA_LOOKAT_TARGET_TRACKS</span>

    </div>

    <div class="block">

    List of keyframe tracks contains multiple camera look-at target
    tracks.

    </div>

    </div>

  - <div id="CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_POSITION_TRACK"
    class="section detail">

    ### CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_POSITION_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_POSITION_TRACK</span>

    </div>

    <div class="block">

    Camera's look-at target is already modified by an earlier track that
    modifies camera's position.

    </div>

    </div>

  - <div id="CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_ORIENTATION_TRACK"
    class="section detail">

    ### CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_ORIENTATION_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_LOOKAT_TARGET_MODIFIED_BY_CAMERA_ORIENTATION_TRACK</span>

    </div>

    <div class="block">

    Camera's look-at target is already modified by an earlier track that
    modifies camera's orientation.

    </div>

    </div>

  - <div id="MULTIPLE_CAMERA_LOOKAT_ORIENTATION_TRACKS"
    class="section detail">

    ### MULTIPLE_CAMERA_LOOKAT_ORIENTATION_TRACKS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">MULTIPLE_CAMERA_LOOKAT_ORIENTATION_TRACKS</span>

    </div>

    <div class="block">

    List of keyframe tracks contains multiple camera look-at orientation
    tracks.

    </div>

    </div>

  - <div id="CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_POSITION_TRACK"
    class="section detail">

    ### CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_POSITION_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_POSITION_TRACK</span>

    </div>

    <div class="block">

    Camera's look-at orientation is already modified by an earlier track
    that modifies camera's position.

    </div>

    </div>

  - <div id="CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_ORIENTATION_TRACK"
    class="section detail">

    ### CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_ORIENTATION_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_LOOKAT_ORIENTATION_MODIFIED_BY_CAMERA_ORIENTATION_TRACK</span>

    </div>

    <div class="block">

    Camera's look-at orientation is already modified by an earlier track
    that modifies camera's orientation.

    </div>

    </div>

  - <div id="MULTIPLE_CAMERA_LOOKAT_DISTANCE_TRACKS"
    class="section detail">

    ### MULTIPLE_CAMERA_LOOKAT_DISTANCE_TRACKS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">MULTIPLE_CAMERA_LOOKAT_DISTANCE_TRACKS</span>

    </div>

    <div class="block">

    List of keyframe tracks contains multiple camera look-at distance
    tracks.

    </div>

    </div>

  - <div id="CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_POSITION_TRACK"
    class="section detail">

    ### CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_POSITION_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_POSITION_TRACK</span>

    </div>

    <div class="block">

    Camera's look-at distance is already modified by an earlier track
    that modifies camera's position.

    </div>

    </div>

  - <div id="CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_ORIENTATION_TRACK"
    class="section detail">

    ### CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_ORIENTATION_TRACK

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">CAMERA_LOOKAT_DISTANCE_MODIFIED_BY_CAMERA_ORIENTATION_TRACK</span>

    </div>

    <div class="block">

    Camera's look-at distance is already modified by an earlier track
    that modifies camera's orientation.

    </div>

    </div>

  - <div id="MULTIPLE_CAMERA_FIELD_OF_VIEW_TRACKS"
    class="section detail">

    ### MULTIPLE_CAMERA_FIELD_OF_VIEW_TRACKS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">MULTIPLE_CAMERA_FIELD_OF_VIEW_TRACKS</span>

    </div>

    <div class="block">

    List of keyframe tracks contains multiple camera field-of-view
    tracks.

    </div>

    </div>

  - <div id="MULTIPLE_CAMERA_FOCAL_LENGTH_TRACKS"
    class="section detail">

    ### MULTIPLE_CAMERA_FOCAL_LENGTH_TRACKS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">MULTIPLE_CAMERA_FOCAL_LENGTH_TRACKS</span>

    </div>

    <div class="block">

    List of keyframe tracks contains multiple camera focal length
    tracks.

    </div>

    </div>

  - <div id="MULTIPLE_CAMERA_PRINCIPAL_POINT_TRACKS"
    class="section detail">

    ### MULTIPLE_CAMERA_PRINCIPAL_POINT_TRACKS

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">MULTIPLE_CAMERA_PRINCIPAL_POINT_TRACKS</span>

    </div>

    <div class="block">

    List of keyframe tracks contains multiple camera principal point
    tracks.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="values()" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the
    order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order
    they are declared

    </div>

  - <div id="valueOf(java.lang.String)" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public
    static</span> <span class="return-type">[MapCameraAnimation.InstantiationErrorCode](sdk-for-android-explore-com-here-sdk-mapview-mapcameraanimation-instantiationerrorcode "enum class in com.here.sdk.mapview")</span> <span class="element-name">valueOf</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The
    string must match exactly an identifier used to declare an enum
    constant in this class. (Extraneous whitespace characters are not
    permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html"
    class="external-link"
    title="class or interface in java.lang"><code>IllegalArgumentException</code></a> -
    if this enum class has no constant with the specified name

    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html"
    class="external-link"
    title="class or interface in java.lang"><code>NullPointerException</code></a> -
    if the argument is null

    </div>

  </div>

</div>

