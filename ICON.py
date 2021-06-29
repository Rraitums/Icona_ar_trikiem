byte_data = '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'