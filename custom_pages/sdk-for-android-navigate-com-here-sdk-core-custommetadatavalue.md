---
title: "CustomMetadataValue (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-custommetadatavalue"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-core-package-summary">com.here.sdk.core</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">CustomMetadataValue</span>

</div>

<div class="block">

Interface for storing arbitrary metadata types. By implementing this interface, multiple object types can be stored as desired, simply by adding fields to the implementation that refer to those objects and then assigning an instance of the CustomMetadataValue derived class to a map item.

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang"><code>String</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      getTag ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Obtains a tag that describes the instance of the interface.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getTag" class="section detail">

    ### getTag

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">getTag</span>()

    </div>

    <div class="block">

    Obtains a tag that describes the instance of the interface. The tag is specific to the concrete implementation of the interface.

    </div>

    Returns:  
    A tag describing the implementation of the interface.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

