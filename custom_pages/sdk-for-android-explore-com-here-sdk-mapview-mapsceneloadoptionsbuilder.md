---
title: "MapSceneLoadOptionsBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapSceneLoadOptionsBuilder →
com.here.NativeBase → com.here.sdk.mapview.MapSceneLoadOptionsBuilder

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapSceneLoadOptionsBuilder</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Builder for creating MapSceneLoadOptions instances. This builder ensures
that either a MapScheme or a configuration file is set, but not both.
Note: This is a beta release of this feature, so there could be a few
bugs and unexpected behaviors. Related APIs may change for new releases
without a deprecation process.

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

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>MapSceneLoadOptionsBuilder.InstantiationErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Describes a reason for failing to build a MapSceneLoadOptions .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationerrordetails"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapSceneLoadOptionsBuilder.InstantiationErrorDetails</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Describes the reason for failing to build a MapSceneLoadOptions .

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapSceneLoadOptionsBuilder.InstantiationException</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Thrown when failing to build a MapSceneLoadOptions .

  </div>

  </div>

  </div>

  </div>
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

      MapSceneLoadOptionsBuilder()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new builder instance.

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

  [`MapSceneLoadOptions`](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptions "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      build()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Builds the MapSceneLoadOptions instance.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withConfigurationFile(String configurationFile)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the configuration file path to load.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withDisabledFeatures(List<String> disabledFeatures)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the features to disable in the new configuration.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withEnabledFeatures(Map<String,String> enabledFeatures)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the features to enable in the new configuration.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withMapScheme(MapScheme mapScheme)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the map scheme to load.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withOverridingMapStyle(Style overridingMapStyle)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the style to override what is defined in the scene configuration.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapSceneLoadOptionsBuilder`](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withWatermarkStyle(WatermarkStyle watermarkStyle)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the watermark style.

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

    ### MapSceneLoadOptionsBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapSceneLoadOptionsBuilder</span>()

    </div>

    <div class="block">

    Creates a new builder instance.

    </div>

    </div>

  </div>
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-withMapScheme(com.here.sdk.mapview.MapScheme)"
    class="section detail">

    ### withMapScheme

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapSceneLoadOptionsBuilder](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withMapScheme</span><span class="parameters">(@NonNull
    [MapScheme](sdk-for-android-explore-com-here-sdk-mapview-mapscheme "enum class in com.here.sdk.mapview") mapScheme)</span>

    </div>

    <div class="block">

    Sets the map scheme to load. Any configuration file set through
    withConfigurationFile(java.lang.String) will be discarded.

    </div>

    Parameters:  
    `mapScheme` -

    Map scheme to load.

    Returns:  
    This class instance.

    </div>
<div id="sdk-for-android-explore-withConfigurationFile(java.lang.String)"
    class="section detail">

    ### withConfigurationFile

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapSceneLoadOptionsBuilder](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withConfigurationFile</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> configurationFile)</span>

    </div>

    <div class="block">

    Sets the configuration file path to load. Any map scheme set through
    withMapScheme(com.here.sdk.mapview.MapScheme) will be discarded.

    </div>

    Parameters:  
    `configurationFile` -

    Configuration file path to load.

    Returns:  
    This class instance.

    </div>
<div id="sdk-for-android-explore-withEnabledFeatures(java.util.Map)"
    class="section detail">

    ### withEnabledFeatures

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapSceneLoadOptionsBuilder](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withEnabledFeatures</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> enabledFeatures)</span>

    </div>

    <div class="block">

    Sets the features to enable in the new configuration.

    </div>

    Parameters:  
    `enabledFeatures` -

    Features to enable. Key = feature name, value = mode name.

    Returns:  
    This class instance.

    </div>
<div id="sdk-for-android-explore-withDisabledFeatures(java.util.List)"
    class="section detail">

    ### withDisabledFeatures

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapSceneLoadOptionsBuilder](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withDisabledFeatures</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a>\<<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a>> disabledFeatures)</span>

    </div>

    <div class="block">

    Sets the features to disable in the new configuration.

    </div>

    Parameters:  
    `disabledFeatures` -

    Features to disable.

    Returns:  
    This class instance.

    </div>
<div id="sdk-for-android-explore-withWatermarkStyle(com.here.sdk.mapview.WatermarkStyle)"
    class="section detail">

    ### withWatermarkStyle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapSceneLoadOptionsBuilder](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withWatermarkStyle</span><span class="parameters">(@NonNull
    [WatermarkStyle](sdk-for-android-explore-com-here-sdk-mapview-watermarkstyle "enum class in com.here.sdk.mapview") watermarkStyle)</span>

    </div>

    <div class="block">

    Sets the watermark style.

    </div>

    Parameters:  
    `watermarkStyle` -

    Watermark style to use.

    Returns:  
    This class instance.

    </div>
<div id="sdk-for-android-explore-withOverridingMapStyle(com.here.sdk.mapview.Style)"
    class="section detail">

    ### withOverridingMapStyle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapSceneLoadOptionsBuilder](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withOverridingMapStyle</span><span class="parameters">(@NonNull
    [Style](sdk-for-android-explore-com-here-sdk-mapview-style "class in com.here.sdk.mapview") overridingMapStyle)</span>

    </div>

    <div class="block">

    Sets the style to override what is defined in the scene
    configuration.

    </div>

    Parameters:  
    `overridingMapStyle` -

    Map style to override the scene configuration.

    Returns:  
    This class instance.

    </div>
<div id="sdk-for-android-explore-build()" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapSceneLoadOptions](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptions "class in com.here.sdk.mapview")</span> <span class="element-name">build</span>()
    throws
    <span class="exceptions">[MapSceneLoadOptionsBuilder.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Builds the MapSceneLoadOptions instance.

    </div>

    Returns:  
    A new MapSceneLoadOptions instance.

    Throws:  
    [`MapSceneLoadOptionsBuilder.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mapsceneloadoptionsbuilder-instantiationexception "class in com.here.sdk.mapview")

    Indicates an instantiation issue.

    </div>

  </div>

</div>

