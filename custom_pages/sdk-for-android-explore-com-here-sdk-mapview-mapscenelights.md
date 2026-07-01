---
title: "MapSceneLights (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapscenelights"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapSceneLights →
com.here.NativeBase → com.here.sdk.mapview.MapSceneLights

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapSceneLights</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Manage the lights and their attributes in a scene.

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
  <td><code>static interface </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingcallback"
  class="type-name-link"
  title="interface in com.here.sdk.mapview"><code>MapSceneLights.AttributeSettingCallback</code></a></td>
  <td><div class="block">
  This callback function allows handling errors that occur during the
  setting of light attributes.
  </div></td>
  </tr>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingerror"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>MapSceneLights.AttributeSettingError</code></a></td>
  <td><div class="block">
  Error enum indicating reasons for failure when setting light attributes.
  </div></td>
  </tr>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-category"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>MapSceneLights.Category</code></a></td>
  <td><div class="block">
  The scene uses three categories of lighting which are: Main light, Back
  light and Rim light.
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-direction"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapSceneLights.Direction</code></a></td>
  <td><div class="block">
  The direction of lights as a pair of azimuth and altitude angles.
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
  <td><a href="sdk-for-android-explore-com-here-sdk-core-color"
  title="class in com.here.sdk.core"><code>Color</code></a></td>
  <td><pre><code>getColor(MapSceneLights.Category category)</code></pre></td>
  <td><div class="block">
  Retrieves the current color of the light based on its category.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-direction"
  title="class in com.here.sdk.mapview"><code>MapSceneLights.Direction</code></a></td>
  <td><pre><code>getDirection(MapSceneLights.Category category)</code></pre></td>
  <td><div class="block">
  Retrieves the current direction of the light based on its category.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><pre><code>getIntensity(MapSceneLights.Category category)</code></pre></td>
  <td><div class="block">
  Retrieves the current intensity of the light based on its category.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>reset()</code></pre></td>
  <td><div class="block">
  Resets all attributes of each light to their default values based on the
  current map scene settings.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setColor(MapSceneLights.Category category,
   Color color,
   MapSceneLights.AttributeSettingCallback callback)</code></pre></td>
  <td><div class="block">
  Set a new color for the light based on its category.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setDirection(MapSceneLights.Category category,
   MapSceneLights.Direction direction,
   MapSceneLights.AttributeSettingCallback callback)</code></pre></td>
  <td><div class="block">
  Set a new direction for the light based on its category.
  </div></td>
  </tr>
  <tr>
  <td><code>void</code></td>
  <td><pre><code>setIntensity(MapSceneLights.Category category,
   double intensity,
   MapSceneLights.AttributeSettingCallback callback)</code></pre></td>
  <td><div class="block">
  Set a new intensity for the light based on its category.
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

- <div id="method-detail" class="section method-details">

  - <div id="setColor(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.core.Color,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)"
    class="section detail">

    ### setColor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setColor</span><span class="parameters">(@NonNull
    [MapSceneLights.Category](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-category "enum class in com.here.sdk.mapview") category,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") color,
    @Nullable
    [MapSceneLights.AttributeSettingCallback](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingcallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Set a new color for the light based on its category.

    </div>

    Parameters:  
    `category` -

    The category of light for which the color is set.

    `color` -

    The Color type includes red, green, blue, and alpha components. The
    value of these components must be inside the range \[0, 1\].

    `callback` -

    Optional callback that will receive the result of this operation.

    </div>

  - <div id="setIntensity(com.here.sdk.mapview.MapSceneLights.Category,double,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)"
    class="section detail">

    ### setIntensity

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setIntensity</span><span class="parameters">(@NonNull
    [MapSceneLights.Category](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-category "enum class in com.here.sdk.mapview") category,
    double intensity, @Nullable
    [MapSceneLights.AttributeSettingCallback](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingcallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Set a new intensity for the light based on its category.

    </div>

    Parameters:  
    `category` -

    The category of light for which the intensity is set.

    `intensity` -

    The light intensity value must be inside the range \[0, 10\]. The
    intensity value is clamped to this range. If the value falls outside
    its supported range, it will be adjusted to stay within the range.
    Note: When the intensity value is big, 3D objects might turn
    completely white because all the color channels could go over the
    limit of 1.0.

    `callback` -

    Optional callback that will receive the result of this operation.

    </div>

  - <div id="setDirection(com.here.sdk.mapview.MapSceneLights.Category,com.here.sdk.mapview.MapSceneLights.Direction,com.here.sdk.mapview.MapSceneLights.AttributeSettingCallback)"
    class="section detail">

    ### setDirection

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDirection</span><span class="parameters">(@NonNull
    [MapSceneLights.Category](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-category "enum class in com.here.sdk.mapview") category,
    @NonNull
    [MapSceneLights.Direction](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-direction "class in com.here.sdk.mapview") direction,
    @Nullable
    [MapSceneLights.AttributeSettingCallback](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingcallback "interface in com.here.sdk.mapview") callback)</span>

    </div>

    <div class="block">

    Set a new direction for the light based on its category.

    </div>

    Parameters:  
    `category` -

    The category of light for which the direction is set.

    `direction` -

    The Direction contains azimuth and altitude angles in degrees.

    `callback` -

    Optional callback that will receive the result of this operation.

    </div>

  - <div id="getColor(com.here.sdk.mapview.MapSceneLights.Category)"
    class="section detail">

    ### getColor

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getColor</span><span class="parameters">(@NonNull
    [MapSceneLights.Category](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-category "enum class in com.here.sdk.mapview") category)</span>

    </div>

    <div class="block">

    Retrieves the current color of the light based on its category.

    </div>

    Parameters:  
    `category` -

    The category of light from which the color is retrieved.

    Returns:  
    The current color of the light, or `null` if the light is missing
    from the loaded scene or MapScene is not intitialized.

    </div>

  - <div id="getIntensity(com.here.sdk.mapview.MapSceneLights.Category)"
    class="section detail">

    ### getIntensity

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">getIntensity</span><span class="parameters">(@NonNull
    [MapSceneLights.Category](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-category "enum class in com.here.sdk.mapview") category)</span>

    </div>

    <div class="block">

    Retrieves the current intensity of the light based on its category.

    </div>

    Parameters:  
    `category` -

    The category of light from which the intensity is retrieved.

    Returns:  
    The current intensity of the light, or `null` if the light is
    missing from the loaded scene or MapScene is not intitialized.

    </div>

  - <div id="getDirection(com.here.sdk.mapview.MapSceneLights.Category)"
    class="section detail">

    ### getDirection

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[MapSceneLights.Direction](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-direction "class in com.here.sdk.mapview")</span> <span class="element-name">getDirection</span><span class="parameters">(@NonNull
    [MapSceneLights.Category](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-category "enum class in com.here.sdk.mapview") category)</span>

    </div>

    <div class="block">

    Retrieves the current direction of the light based on its category.

    </div>

    Parameters:  
    `category` -

    The category of light from which the direction is retrieved.

    Returns:  
    The current direction of the light, or `null` if the light is
    missing from the loaded scene or MapScene is not intitialized.

    </div>

  - <div id="reset()" class="section detail">

    ### reset

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">reset</span>()

    </div>

    <div class="block">

    Resets all attributes of each light to their default values based on
    the current map scene settings.

    </div>

    </div>

  </div>

</div>

