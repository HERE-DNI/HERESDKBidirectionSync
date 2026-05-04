---
title: "CustomMetadataValue (API Reference)"
slug: "sdk-for-android-explore-api-reference-latestcustommetadatavalue"
hidden: false
---

Package [com.here.sdk.core](sdk-for-android-explore-api-reference-latestpackage-summary)

# Interface CustomMetadataValue

------------------------------------------------------------------------
public interface CustomMetadataValue
Interface for storing arbitrary metadata types. By implementing this interface, multiple object types can be stored as desired, simply by adding fields to the implementation that refer to those objects and then assigning an instance of the CustomMetadataValue derived class to a map item.

## Method Summary

  All Methods
  Instance Methods
  Abstract Methods

  Modifier and Type

  Method

  Description

  [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html)

  [getTag](#getTag())`()`

Obtains a tag that describes the instance of the interface.

## Method Details

### getTag

@NonNull [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html) getTag()

    Obtains a tag that describes the instance of the interface. The tag is specific to the concrete implementation of the interface.
Returns:
    A tag describing the implementation of the interface.
