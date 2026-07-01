---
title: "MapSceneLights.AttributeSettingCallback (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapscenelights-attributesettingcallback"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div id="class-description" class="section class-description">

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

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Instance Methods
  Abstract Methods

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
  <td><code>void</code></td>
  <td><pre><code>onAttributeSetting(MapSceneLights.AttributeSettingError setLightError)</code></pre></td>
  <td><div class="block">
  This callback function allows handling errors that occur during the
  setting of light attributes.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  </div>

</div>

<div class="section details">

- <div id="method-detail" class="section method-details">

  - <div id="onAttributeSetting(com.here.sdk.mapview.MapSceneLights.AttributeSettingError)"
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

