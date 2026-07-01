---
title: "MapFeatureModes (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.MapFeatureModes

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapFeatureModes</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Holds constants for map feature modes, to be used with
MapScene.enableFeatures(java.util.Map ) . Use DEFAULT to enable a
feature with its default mode. Note: The default mode is defined by the
currently loaded map scene configuration and may vary per MapScheme .
The currently active features and modes can be inspected using
MapScene.getActiveFeatures() after the scene is loaded. See MapFeatures
for constants representing the feature names.

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
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#AMBIENT_OCCLUSION_ALL"
  class="member-name-link"><code>AMBIENT_OCCLUSION_ALL</code></a></td>
  <td><div class="block">
  Ambient occlusion effect is shown for extruded buildings and landmarks.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#BUILDING_FOOTPRINTS_ALL"
  class="member-name-link"><code>BUILDING_FOOTPRINTS_ALL</code></a></td>
  <td><div class="block">
  All building footprints are shown.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#CONGESTION_ZONES_ALL"
  class="member-name-link"><code>CONGESTION_ZONES_ALL</code></a></td>
  <td><div class="block">
  All congestion zones are shown.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#DEFAULT"
  class="member-name-link"><code>DEFAULT</code></a></td>
  <td><div class="block">
  Enables the default mode of a map feature.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#ENVIRONMENTAL_ZONES_ALL"
  class="member-name-link"><code>ENVIRONMENTAL_ZONES_ALL</code></a></td>
  <td><div class="block">
  All environmental zones are shown.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#EXTRUDED_BUILDINGS_ALL"
  class="member-name-link"><code>EXTRUDED_BUILDINGS_ALL</code></a></td>
  <td><div class="block">
  All extruded buildings are shown.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#LOW_SPEED_ZONES_ALL"
  class="member-name-link"><code>LOW_SPEED_ZONES_ALL</code></a></td>
  <td><div class="block">
  All low speed zones are shown.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#ROAD_EXIT_LABELS_ALL"
  class="member-name-link"><code>ROAD_EXIT_LABELS_ALL</code></a></td>
  <td><div class="block">
  Road exit labels are shown with numbers and names, if available.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#ROAD_EXIT_LABELS_NUMBERS_ONLY"
  class="member-name-link"><code>ROAD_EXIT_LABELS_NUMBERS_ONLY</code></a></td>
  <td><div class="block">
  Road exit labels are shown with numbers, if available.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#SHADOWS_ALL"
  class="member-name-link"><code>SHADOWS_ALL</code></a></td>
  <td><div class="block">
  Shadows are shown for extruded buildings and landmarks.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW"
  class="member-name-link"><code>TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</code></a></td>
  <td><div class="block">
  Only available when Japan map is used.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITH_FREE_FLOW"
  class="member-name-link"><code>TRAFFIC_FLOW_WITH_FREE_FLOW</code></a></td>
  <td><div class="block">
  Traffic flow shows green lines when there is no traffic congestion.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_FLOW_WITHOUT_FREE_FLOW"
  class="member-name-link"><code>TRAFFIC_FLOW_WITHOUT_FREE_FLOW</code></a></td>
  <td><div class="block">
  Traffic flow does not show green lines when there is no traffic
  congestion.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_INCIDENTS_ALL"
  class="member-name-link"><code>TRAFFIC_INCIDENTS_ALL</code></a></td>
  <td><div class="block">
  All available traffic incidents are shown.
  </div></td>
  </tr>
  <tr>
  <td><code>static final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapfeaturemodes#TRAFFIC_LIGHTS_ALL"
  class="member-name-link"><code>TRAFFIC_LIGHTS_ALL</code></a></td>
  <td><div class="block">
  All available traffic lights are shown.
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
  <td><pre><code>MapFeatureModes()</code></pre></td>
  <td> </td>
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

  - <div id="DEFAULT" class="section detail">

    ### DEFAULT

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">DEFAULT</span>

    </div>

    <div class="block">

    Enables the default mode of a map feature. Can be used with any map
    feature.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.DEFAULT)

    </div>

  - <div id="BUILDING_FOOTPRINTS_ALL" class="section detail">

    ### BUILDING_FOOTPRINTS_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">BUILDING_FOOTPRINTS_ALL</span>

    </div>

    <div class="block">

    All building footprints are shown.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.BUILDING_FOOTPRINTS_ALL)

    </div>

  - <div id="CONGESTION_ZONES_ALL" class="section detail">

    ### CONGESTION_ZONES_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">CONGESTION_ZONES_ALL</span>

    </div>

    <div class="block">

    All congestion zones are shown.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.CONGESTION_ZONES_ALL)

    </div>

  - <div id="EXTRUDED_BUILDINGS_ALL" class="section detail">

    ### EXTRUDED_BUILDINGS_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">EXTRUDED_BUILDINGS_ALL</span>

    </div>

    <div class="block">

    All extruded buildings are shown.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.EXTRUDED_BUILDINGS_ALL)

    </div>

  - <div id="ENVIRONMENTAL_ZONES_ALL" class="section detail">

    ### ENVIRONMENTAL_ZONES_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">ENVIRONMENTAL_ZONES_ALL</span>

    </div>

    <div class="block">

    All environmental zones are shown.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.ENVIRONMENTAL_ZONES_ALL)

    </div>

  - <div id="LOW_SPEED_ZONES_ALL" class="section detail">

    ### LOW_SPEED_ZONES_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">LOW_SPEED_ZONES_ALL</span>

    </div>

    <div class="block">

    All low speed zones are shown.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.LOW_SPEED_ZONES_ALL)

    </div>

  - <div id="TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW"
    class="section detail">

    ### TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW</span>

    </div>

    <div class="block">

    Only available when Japan map is used. Traffic flow shows green
    lines depending on the region. In Japan green lines will not be
    shown, as if the TRAFFIC_FLOW_WITHOUT_FREE_FLOW were used. In rest
    of the world, green lines will be shown, as if the
    TRAFFIC_FLOW_WITH_FREE_FLOW were used.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_JAPAN_WITHOUT_FREE_FLOW)

    </div>

  - <div id="TRAFFIC_FLOW_WITH_FREE_FLOW" class="section detail">

    ### TRAFFIC_FLOW_WITH_FREE_FLOW

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW_WITH_FREE_FLOW</span>

    </div>

    <div class="block">

    Traffic flow shows green lines when there is no traffic congestion.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITH_FREE_FLOW)

    </div>

  - <div id="TRAFFIC_FLOW_WITHOUT_FREE_FLOW" class="section detail">

    ### TRAFFIC_FLOW_WITHOUT_FREE_FLOW

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_FLOW_WITHOUT_FREE_FLOW</span>

    </div>

    <div class="block">

    Traffic flow does not show green lines when there is no traffic
    congestion.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_FLOW_WITHOUT_FREE_FLOW)

    </div>

  - <div id="TRAFFIC_INCIDENTS_ALL" class="section detail">

    ### TRAFFIC_INCIDENTS_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_INCIDENTS_ALL</span>

    </div>

    <div class="block">

    All available traffic incidents are shown.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_INCIDENTS_ALL)

    </div>

  - <div id="TRAFFIC_LIGHTS_ALL" class="section detail">

    ### TRAFFIC_LIGHTS_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">TRAFFIC_LIGHTS_ALL</span>

    </div>

    <div class="block">

    All available traffic lights are shown.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.TRAFFIC_LIGHTS_ALL)

    </div>

  - <div id="ROAD_EXIT_LABELS_NUMBERS_ONLY" class="section detail">

    ### ROAD_EXIT_LABELS_NUMBERS_ONLY

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">ROAD_EXIT_LABELS_NUMBERS_ONLY</span>

    </div>

    <div class="block">

    Road exit labels are shown with numbers, if available.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_NUMBERS_ONLY)

    </div>

  - <div id="ROAD_EXIT_LABELS_ALL" class="section detail">

    ### ROAD_EXIT_LABELS_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">ROAD_EXIT_LABELS_ALL</span>

    </div>

    <div class="block">

    Road exit labels are shown with numbers and names, if available.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.ROAD_EXIT_LABELS_ALL)

    </div>

  - <div id="SHADOWS_ALL" class="section detail">

    ### SHADOWS_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">SHADOWS_ALL</span>

    </div>

    <div class="block">

    Shadows are shown for extruded buildings and landmarks. Note: This
    is a beta release of this feature, so there could be a few bugs and
    unexpected behavior. Related APIs may change for new releases
    without a deprecation process.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.SHADOWS_ALL)

    </div>

  - <div id="AMBIENT_OCCLUSION_ALL" class="section detail">

    ### AMBIENT_OCCLUSION_ALL

    <div class="member-signature">

    <span class="modifiers">public static
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">AMBIENT_OCCLUSION_ALL</span>

    </div>

    <div class="block">

    Ambient occlusion effect is shown for extruded buildings and
    landmarks. Note: This is a beta release of this feature, so there
    could be a few bugs and unexpected behavior. Related APIs may change
    for new releases without a deprecation process.

    </div>

    See Also:  
    - [Constant Field
      Values](sdk-for-android-explore-constant-values#com.here.sdk.mapview.MapFeatureModes.AMBIENT_OCCLUSION_ALL)

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### MapFeatureModes

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapFeatureModes</span>()

    </div>

    </div>

  </div>

</div>

