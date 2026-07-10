---
title: "CustomWarningProvider (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-customwarningprovider"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-warner-package-summary">com.here.sdk.warner</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">CustomWarningProvider</span>

</div>

<div class="block">

A interface representing a provider of custom warnings based on vehicle position. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getCustomWarningType ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Returns the custom warning type identifier produced by this provider.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-warner-customwarning" title="class in com.here.sdk.warner">`CustomWarning`</a>`>`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getWarnings ( SegmentData currentSegment, SegmentData previousSegment)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Returns a list of custom warnings for the given vehicle position.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getCustomWarningType" class="section detail">

    ### getCustomWarningType

    <div class="member-signature">

    <span class="return-type">int</span> <span class="element-name">getCustomWarningType</span>()

    </div>

    <div class="block">

    Returns the custom warning type identifier produced by this provider. The returned value corresponds to CustomWarning.customWarningType and Warning.customWarningType and is used to apply per-type configuration, such as notification distances.

    </div>

    Returns:  
    The custom warning type identifier for this provider.

    </div>

  - <div id="sdk-for-android-navigate-getWarnings-com-here-sdk-mapdata-SegmentData-com-here-sdk-mapdata-SegmentData" class="section detail">

    ### getWarnings

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-warner-customwarning" title="class in com.here.sdk.warner">CustomWarning</a>\></span> <span class="element-name">getWarnings</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a> currentSegment, @Nullable <a href="sdk-for-android-navigate-com-here-sdk-mapdata-segmentdata" title="class in com.here.sdk.mapdata">SegmentData</a> previousSegment)</span>

    </div>

    <div class="block">

    Returns a list of custom warnings for the given vehicle position. This method evaluates the custom warning provider using the current vehicle position on the electronic horizon and returns the resulting custom warnings along with corresponding payload.

    </div>

    Parameters:  
    `currentSegment` -

    Segment data representing the vehicle’s current position on the electronic horizon.

    `previousSegment` -

    Segment data representing the vehicle’s previous position on the electronic horizon. This parameter may be null if no previous position information is available.

    Returns:  
    A list of `CustomWarning` instances representing all applicable custom warnings. The list may be empty if no warnings apply.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

