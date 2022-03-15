
/**
  ******************************************************************************
  * @file    aitest_data.h
  * @author  AST Embedded Analytics Research Platform
  * @date    Tue Mar 15 10:32:14 2022
  * @brief   AI Tool Automatic Code Generator for Embedded NN computing
  ******************************************************************************
  * Copyright (c) 2017 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  ******************************************************************************
  */

#ifndef AITEST_DATA_H
#define AITEST_DATA_H
#pragma once

#include "aitest_config.h"
#include "ai_platform.h"

#define AI_AITEST_DATA_CONFIG               (NULL)


#define AI_AITEST_DATA_ACTIVATIONS_SIZES \
  { 384, }
#define AI_AITEST_DATA_ACTIVATIONS_SIZE     (384)
#define AI_AITEST_DATA_ACTIVATIONS_COUNT    (1)
#define AI_AITEST_DATA_ACTIVATION_1_SIZE    (384)



#define AI_AITEST_DATA_WEIGHTS_SIZES \
  { 45580, }
#define AI_AITEST_DATA_WEIGHTS_SIZE         (45580)
#define AI_AITEST_DATA_WEIGHTS_COUNT        (1)
#define AI_AITEST_DATA_WEIGHT_1_SIZE        (45580)



AI_DEPRECATED
#define AI_AITEST_DATA_ACTIVATIONS(ptr_)  \
  ai_aitest_data_activations_buffer_get(AI_HANDLE_PTR(ptr_))

AI_DEPRECATED
#define AI_AITEST_DATA_WEIGHTS(ptr_)  \
  ai_aitest_data_weights_buffer_get(AI_HANDLE_PTR(ptr_))


AI_API_DECLARE_BEGIN

/*!
 * @brief Get network activations buffer initialized struct.
 * @ingroup aitest_data
 * @param[in] ptr a pointer to the activations array storage area
 * @return an ai_buffer initialized struct
 */
AI_DEPRECATED
AI_API_ENTRY
ai_buffer ai_aitest_data_activations_buffer_get(const ai_handle ptr);

/*!
 * @brief Get network weights buffer initialized struct.
 * @ingroup aitest_data
 * @param[in] ptr a pointer to the weights array storage area
 * @return an ai_buffer initialized struct
 */
AI_DEPRECATED
AI_API_ENTRY
ai_buffer ai_aitest_data_weights_buffer_get(const ai_handle ptr);

/*!
 * @brief Get network weights array pointer as a handle ptr.
 * @ingroup aitest_data
 * @return a ai_handle pointer to the weights array
 */
AI_DEPRECATED
AI_API_ENTRY
ai_handle ai_aitest_data_weights_get(void);


/*!
 * @brief Get network params configuration data structure.
 * @ingroup aitest_data
 * @return true if a valid configuration is present, false otherwise
 */
AI_API_ENTRY
ai_bool ai_aitest_data_params_get(ai_network_params* params);


AI_API_DECLARE_END

#endif /* AITEST_DATA_H */

