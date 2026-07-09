---
title: "WarningListener (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-warninglistener"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-warner-package-summary">com.here.sdk.warner</a>

</div>

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public interface </span><span class="element-name type-name-label">WarningListener</span>

</div>

<div class="block">

A generic listener interface interface for receiving warning notifications. Implementations of this interface are notified whenever the WarnerEngine detects new warnings. The listener receives a list of Warning objects, each describing a specific event or condition that requires user attention. Classes interested in warning updates should implement this listener and register themselves via WarnerEngine.addWarningListener . Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

      onWarnings ( List < Warning > warnings)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab3">

  <div class="block">

  Called when a new warnings is detected.

  </div>

  </div>

  </div>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-onWarnings-java-util-List" class="section detail">

    ### onWarnings

    <div class="member-signature">

    <span class="return-type">void</span> <span class="element-name">onWarnings</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a>\> warnings)</span>

    </div>

    <div class="block">

    Called when a new warnings is detected. This method is invoked whenever a new list of warnings becomes available.

    </div>

    Parameters:  
    `warnings` -

    The list of warning objects containing details about each warning.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->

