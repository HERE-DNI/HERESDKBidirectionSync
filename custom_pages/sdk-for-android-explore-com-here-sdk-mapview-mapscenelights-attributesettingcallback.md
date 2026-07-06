---
title: "MapSceneLights.AttributeSettingCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingcallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[MapSceneLights](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights "class in com.here.sdk.mapview")

<!-- -->

Functional Interface:  
This is a functional interface and can therefore be used as the
assignment target for a lambda expression or method reference.

<div class="type-signature">

<span class="annotations"><a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/FunctionalInterface.html"
class="external-link"
title="class or interface in java.lang">@FunctionalInterface</a>
</span><span class="modifiers">public static interface
</span><span class="element-name type-name-label">MapSceneLights.AttributeSettingCallback</span>

</div>

<div class="block">

This callback function allows handling errors that occur during the
setting of light attributes.

</div>

</div>

<div class="section summary">
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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onAttributeSetting(MapSceneLights.AttributeSettingError setLightError)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  This callback function allows handling errors that occur during the
  setting of light attributes.

  </div>

  </div>

  </div>

  </div>

  </div>

</div>

<div class="section details">
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-onAttributeSetting(com.here.sdk.mapview.MapSceneLights.AttributeSettingError)"
    class="section detail">

    ### onAttributeSetting

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onAttributeSetting</span><span class="parameters">(@Nullable
    [MapSceneLights.AttributeSettingError](sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingerror "enum class in com.here.sdk.mapview") setLightError)</span>

    </div>

    <div class="block">

    This callback function allows handling errors that occur during the
    setting of light attributes.

    </div>

    Parameters:  
    `setLightError` -

    The cause for the failure when setting the light attributes, or
    `null` if no error occurred. Note: The error code `NO_LIGHTS` may be
    returned when attempting to set light attributes in map schemes that
    do not support lights, for instance `road.network` map scheme.
    Please refer to the error code documentation for further details on
    error handling.

    </div>

  </div>

</div>

